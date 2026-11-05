import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/context-bridge/scripts/context_package.py"
SPEC = importlib.util.spec_from_file_location("context_package", SCRIPT)
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)
BASE = json.loads((ROOT / "tests/fixtures/T19/context.json").read_text(encoding="utf-8"))


class ContextPackageTests(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(BASE)

    def test_valid_unicode_and_unknown_dates(self):
        self.data["items"][0]["content"] = "保留原始文档；SQLite enables offline search."
        self.data["items"][0]["date"] = None
        self.data["sources"][0]["date"] = None
        self.assertEqual(PACKAGE.validate(self.data), [])
        files = PACKAGE.build_files(self.data)
        self.assertIn("保留原始文档", files["DECISIONS.md"])
        self.assertIn("Date: unknown", files["DECISIONS.md"])

    def test_required_types_unknown_fields_and_whitespace(self):
        mutations = [lambda d: d.pop("scope"), lambda d: d.update(items="not an array"),
                     lambda d: d["items"][0].update(content=" \n "),
                     lambda d: d["items"][0].update(unexpected="x"),
                     lambda d: d["items"][0].update(evidence=[]),
                     lambda d: d.update(items=[])]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data = copy.deepcopy(self.data)
                mutate(data)
                self.assertTrue(PACKAGE.validate(data))

    def test_duplicate_ids_and_evidence(self):
        for field in ("items", "sources"):
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data[field].append(copy.deepcopy(data[field][0]))
                self.assertTrue(PACKAGE.validate(data))
        self.data["items"][0]["evidence"] *= 2
        self.assertTrue(PACKAGE.validate(self.data))

    def test_bad_dates_and_missing_timezone(self):
        for value in ("2026-02-30", "2026-13-01", "tomorrow", "2026-1-1"):
            with self.subTest(value=value):
                self.data["items"][0]["date"] = value
                self.assertTrue(PACKAGE.validate(self.data))
        self.data = copy.deepcopy(BASE)
        for value in ("2026-01-01T10:00:00", "2026-01-01", "2026-02-30T10:00:00Z",
                      "2026-01-01T10:00:00+00:60", "2026-01-01T10:00:00+24:00"):
            with self.subTest(value=value):
                self.data["generated_at"] = value
                self.assertTrue(PACKAGE.validate(self.data))

    def test_fractional_timestamp_precision_is_preserved(self):
        for fraction in ("", ".1", ".12", ".123", ".1234", ".12345", ".123456", ".3889904", ".123456789"):
            for timezone in ("Z", "+08:00", "-05:30"):
                value = "2026-11-05T12:30:07" + fraction + timezone
                with self.subTest(value=value):
                    self.data["generated_at"] = value
                    self.assertEqual(PACKAGE.validate(self.data), [])
                    rendered = json.loads(PACKAGE.build_files(self.data)["context.json"])
                    self.assertEqual(rendered["generated_at"], value)

    def test_recorded_context_packages_validate(self):
        paths = [path for path in (ROOT / "tests/actual").glob("*/output/**/*.json")
                 if path.name in ("context.json", "context.v1.json", "full-review-candidates.json")]
        self.assertTrue(paths, "Recorded live context packages must be present")
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(PACKAGE.validate(PACKAGE.read_json(path)), [])

    def test_missing_source_is_not_fabricated(self):
        self.data["items"][0]["evidence"][0]["source_id"] = "missing-source"
        self.assertTrue(PACKAGE.validate(self.data))

    def test_inferences_cannot_be_verified(self):
        item = self.data["items"][0]
        item.update(category="inference", confidence="verified")
        self.assertTrue(PACKAGE.validate(self.data))
        item["confidence"] = "inferred"
        self.assertEqual(PACKAGE.validate(self.data), [])
        item["category"] = "fact"
        self.assertTrue(PACKAGE.validate(self.data))

    def test_project_and_work_scopes(self):
        item = self.data["items"][0]
        for scope in ("work", "personal"):
            item["scope"] = scope
            self.assertTrue(PACKAGE.validate(self.data))
        self.data["scope"] = "work"
        self.assertTrue(PACKAGE.validate(self.data))
        item["scope"] = "work"
        self.assertEqual(PACKAGE.validate(self.data), [])
        self.data["scope"] = "personal"
        item["scope"] = "personal"
        self.assertEqual(PACKAGE.validate(self.data), [])

    def test_sensitive_labels_are_rejected(self):
        for sensitivity in ("sensitive", "credential"):
            self.data["items"][0]["sensitivity"] = sensitivity
            self.assertTrue(PACKAGE.validate(self.data))

    def test_secrets_block_render_without_echo(self):
        # Nonfunctional synthetic sentinels. No real secrets belong in tests.
        secrets = ["sk-proj-TEST_SENTINEL_000000000000000000", "ghp_TEST_SENTINEL_00000000000000",
                   "API_KEY=synthetic-private-value", "password: fictional-test-only",
                   "token=synthetic-private-value", "secret=x", "密码=中",
                   "-----BEGIN PRIVATE KEY-----", "https://user:fixture-password@example.invalid",
                   "4111 1111 1111 1111", "110101199001010011"]
        for secret in secrets:
            with self.subTest(kind=secret.split("-")[0][:8]):
                data = copy.deepcopy(self.data)
                data["items"][0]["content"] = "Useful context. " + secret
                errors = PACKAGE.validate(data)
                self.assertTrue(errors)
                self.assertNotIn(secret, " ".join(errors))
                with self.assertRaises(PACKAGE.PackageError):
                    PACKAGE.build_files(data)

    def test_secrets_in_source_labels_locations_and_unknown_keys(self):
        secret = "sk-proj-TEST_SENTINEL_000000000000000000"
        mutations = [lambda d: d["sources"][0].update(label=secret),
                     lambda d: d["items"][0]["evidence"][0].update(locator=secret),
                     lambda d: d.update({secret: "hidden in an unknown key"})]
        for mutate in mutations:
            data = copy.deepcopy(self.data)
            mutate(data)
            errors = PACKAGE.validate(data)
            self.assertTrue(errors)
            self.assertNotIn(secret, " ".join(errors))

    def add_second(self, status="current"):
        second = copy.deepcopy(self.data["items"][0])
        second.update(id="ctx-second", content="Harbor uses SQLite FTS5.", status=status)
        self.data["items"].append(second)
        return second

    def test_unresolved_conflict_kept_out_of_current_decisions(self):
        first = self.data["items"][0]
        first["status"] = "conflict"
        second = self.add_second("conflict")
        self.data["conflicts"] = [{"id": "conflict-1", "item_ids": [first["id"], second["id"]],
                                   "question": "Which storage decision is effective?", "resolution": None}]
        self.assertEqual(PACKAGE.validate(self.data), [])
        files = PACKAGE.build_files(self.data)
        self.assertNotIn("DECISIONS.md", files)
        self.assertIn("ctx-original", files["OPEN_QUESTIONS.md"])
        self.assertIn("ctx-second", files["OPEN_QUESTIONS.md"])
        self.assertIn("unresolved", files["OPEN_QUESTIONS.md"])

    def test_conflict_group_integrity(self):
        self.data["items"][0]["status"] = "conflict"
        self.assertTrue(PACKAGE.validate(self.data))
        self.add_second()
        self.data["conflicts"] = [{"id": "conflict-1", "item_ids": ["ctx-original", "ctx-second"],
                                   "question": "Which?", "resolution": None}]
        self.assertTrue(PACKAGE.validate(self.data))
        self.data["items"][1]["status"] = "conflict"
        self.assertEqual(PACKAGE.validate(self.data), [])
        self.data["conflicts"][0]["item_ids"][1] = "unknown"
        self.assertTrue(PACKAGE.validate(self.data))

    def test_supersession_preserves_history_and_rationale(self):
        self.data["items"][0]["status"] = "historical"
        second = self.add_second()
        second["supersedes"] = ["ctx-original"]
        self.data["conflicts"] = [{"id": "conflict-1", "item_ids": ["ctx-original", "ctx-second"],
                                   "question": "Which index?", "resolution": "Accepted migration in supplied decision."}]
        self.assertEqual(PACKAGE.validate(self.data), [])
        files = PACKAGE.build_files(self.data)
        self.assertIn("JSON-file", files["HISTORY.md"])
        self.assertIn("Accepted migration", files["HISTORY.md"])
        self.assertIn("SQLite FTS5", files["DECISIONS.md"])

    def test_invalid_supersession_and_cycles(self):
        item = self.data["items"][0]
        for predecessor in ("missing", "ctx-original"):
            item["supersedes"] = [predecessor]
            self.assertTrue(PACKAGE.validate(self.data))
        second = self.add_second("historical")
        item.update(status="historical", supersedes=["ctx-second"])
        second["supersedes"] = ["ctx-original"]
        self.assertIn("$: supersession cycle", PACKAGE.validate(self.data))

    def test_historical_category_cannot_look_current(self):
        self.data["items"][0].update(category="historical", status="current")
        self.assertTrue(PACKAGE.validate(self.data))

    def test_stale_task_goes_to_history(self):
        self.data["items"][0].update(category="temporary", area="task", status="stale")
        files = PACKAGE.build_files(self.data)
        self.assertIn("HISTORY.md", files)
        self.assertNotIn("CURRENT_TASKS.md", files)

    def test_full_review_cannot_render_before_selection(self):
        self.data.update(scope="full-review", review_status="candidate")
        self.assertEqual(PACKAGE.validate(self.data), [])
        with self.assertRaises(PACKAGE.PackageError):
            PACKAGE.build_files(self.data)

    def test_no_empty_topic_files_or_raw_sources(self):
        files = PACKAGE.build_files(self.data)
        self.assertEqual(set(files), {"README.md", "DECISIONS.md", "HANDOFF.md", "context.json"})
        self.assertLess(len(files["HANDOFF.md"].split()), 180)
        self.assertNotIn("CONSTRAINTS.md", files["HANDOFF.md"])

    def test_host_adapters_are_inert(self):
        for target in ("codex", "claude-code"):
            self.data["target"] = target
            files = PACKAGE.build_files(self.data)
            self.assertIn(f"adapters/{target}.md", files)
            self.assertNotIn("AGENTS.md", files)
            self.assertNotIn("CLAUDE.md", files)

    def test_markdown_content_is_not_rendered_as_html_or_commands(self):
        self.data["items"][0]["content"] = '<script>alert(1)</script>\n# Not a heading\n![link](https://example.invalid)'
        rendered = PACKAGE.build_files(self.data)["DECISIONS.md"]
        self.assertNotIn("<script>", rendered)
        self.assertNotIn("\n# Not a heading", rendered)
        self.assertNotIn("![link]", rendered)

    def test_cli_roundtrip_preserves_input_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
            root = Path(directory)
            source = root / "source.json"
            original = json.dumps(self.data, ensure_ascii=False).encode("utf-8")
            source.write_bytes(original)
            output = root / "package with spaces"
            command = [sys.executable, str(SCRIPT), "render", str(source), "--output", str(output)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            audit = subprocess.run([sys.executable, str(SCRIPT), "validate", str(output)], capture_output=True, text=True)
            self.assertEqual(audit.returncode, 0, audit.stderr)
            snapshot = {p.name: p.read_bytes() for p in output.iterdir()}
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(snapshot, {p.name: p.read_bytes() for p in output.iterdir()})

    def test_directory_drift_missing_extra_and_sensitive_files(self):
        for mutation in ("drift", "missing", "extra", "secret"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
                output = Path(directory) / "package"
                PACKAGE.render(self.data, output)
                if mutation == "drift":
                    (output / "DECISIONS.md").write_text("Changed claim", encoding="utf-8")
                elif mutation == "missing":
                    (output / "HANDOFF.md").unlink()
                elif mutation == "extra":
                    (output / "unreviewed.txt").write_text("Extra private notes", encoding="utf-8")
                else:
                    (output / "README.md").write_text("password: synthetic-only", encoding="utf-8")
                self.assertTrue(PACKAGE.validate_path(output))

    def test_invalid_data_creates_no_output(self):
        self.data["items"][0]["content"] = "password: synthetic-only"
        with tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
            output = Path(directory) / "package"
            with self.assertRaises(PACKAGE.PackageError):
                PACKAGE.render(self.data, output)
            self.assertFalse(output.exists())

    def test_duplicate_json_keys_nan_and_invalid_json_are_safe_errors(self):
        payloads = ['{"scope":"work","scope":"personal"}', '{"value": NaN}', 'sk-proj-TEST_SENTINEL_000000000000000000']
        for payload in payloads:
            with tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
                path = Path(directory) / "input.json"
                path.write_text(payload, encoding="utf-8")
                proc = subprocess.run([sys.executable, str(SCRIPT), "validate", str(path)], capture_output=True, text=True)
                self.assertNotEqual(proc.returncode, 0)
                self.assertNotIn(payload, proc.stderr + proc.stdout)
                self.assertNotIn("Traceback", proc.stderr)

    def test_utf8_bom_is_accepted(self):
        with tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
            path = Path(directory) / "input.json"
            path.write_text(json.dumps(self.data), encoding="utf-8-sig")
            self.assertEqual(PACKAGE.validate_path(path), [])

    def test_symlink_input_is_not_followed(self):
        with tempfile.TemporaryDirectory(prefix="context-bridge-test-") as directory:
            root = Path(directory)
            real = root / "real.json"
            real.write_text(json.dumps(self.data), encoding="utf-8")
            link = root / "link.json"
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("Creating symlinks is not permitted by this platform")
            with self.assertRaises(PACKAGE.PackageError):
                PACKAGE.validate_path(link)


if __name__ == "__main__":
    unittest.main()
