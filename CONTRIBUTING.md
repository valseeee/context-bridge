# Contributing

Keep the Skill focused on context portability. A change should improve a real
extraction, classification, privacy, update or handoff outcome. Avoid adding
account scrapers, automatic uploads, model providers or persistent-memory hooks.

Use Python 3.10+ for the optional helper and test suite. The runtime and tests use
the standard library; no package installation is needed.

```sh
python -m unittest discover -s tests -v
python tests/check_skill.py
```

Add a synthetic scenario when behavior changes. Preserve its raw input, expected
behavior, actual artifacts, Pass/Fail and failure notes. See
[evaluation.md](tests/evaluation.md). Do not claim a helper unit test proves the
AI model extracted the right facts or that a new host is supported.

The opt-in live runner uses an already authenticated Codex CLI and can consume
usage allowance. It copies only synthetic fixtures and the skill into isolated
workspaces; it must never be pointed at private transcripts. Choose a fresh run
directory in your usual temporary workspace:

```sh
python tests/run_live.py --cases T01 T04 T10 T12 T16 --run-root /your/temp/context-bridge-run
python tests/assess_live.py /your/temp/context-bridge-run
```

The runner keeps raw traces locally. Publish only reviewed synthetic outputs and
compact run metadata. A successful process exit is not a successful scenario;
inspect actual files and their meaning. Installation, explicit invocation and
implicit triggering each require observable evidence.

For a release, run `python scripts/build_release.py`. The resulting ZIP contains
only the installable skill and its license, and has a SHA-256 sidecar. Test an
extracted copy before attaching it to a release. Do not include private packages
or raw evaluation traces.

For bug reports, state host/version, OS, reproduction, expected and observed
behavior. Redact personal data. Report security issues as described in
[SECURITY.md](SECURITY.md). Pull requests should describe the user-visible change,
why it matters and the checks actually executed.

Do not silently change schema version 1.0. Keep the JSON Schema, helper contract,
examples and tests aligned. For additional JSON Schema vocabulary, update the
validator or use an established implementation before claiming support.
