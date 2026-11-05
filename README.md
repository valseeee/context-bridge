# Your AI Knows You.

**Take Your AI Context Anywhere.**

ContextBridge turns selected conversations and project documents into a portable,
reviewable context package. Keep your decisions, constraints and next steps when
you switch assistants. **AI 记忆搬运工 — [中文说明](README.zh-CN.md)**

[Download the Skill](https://github.com/valseeee/context-bridge/releases/latest) ·
[Inspect a real test output](tests/actual/T02/output/context-package/README.md) ·
[Validation record](tests/evaluation.md)

```text
Conversations + project notes
          ↓
Extract → classify → verify → resolve → package
          ↓
Markdown + structured JSON + a short handoff
          ↓
Continue the existing work in your next assistant
```

ContextBridge is an open-source **Agent Skill**, not a service or a chat-history
scraper. Your AI host performs semantic extraction. An optional Python helper
validates and renders the selected context locally with no third-party dependencies.

## Try it

Install the entire [skill folder](skills/context-bridge), then provide a Markdown
file, TXT, README, decision notes, or pasted conversation:

```text
Use $context-bridge to create a portable context package from these notes.
Keep only this project's context, preserve decisions and constraints,
and prepare a handoff for Codex. Save it in a new context-package directory.
```

In Claude Code use `/context-bridge` instead. In a host without file tools, paste
the input and ask for labelled file contents. Do not paste credentials.

## Install

Download the release ZIP or clone this repository. Copy the **whole**
`skills/context-bridge` folder, including references and scripts, to one destination:

| Host | Project-local destination | Invoke |
| --- | --- | --- |
| Codex | `.agents/skills/context-bridge/` | `$context-bridge` |
| Claude Code | `.claude/skills/context-bridge/` | `/context-bridge` |

Codex installation, selection and output have been exercised in live CLI tests.
Claude Code's documented installation format is included; its runtime has not
been tested in this environment.

Run from the cloned repository, replacing `/path/to/project` with your project:

```sh
destination=/path/to/project/.agents/skills/context-bridge
if [ -e "$destination" ]; then
  echo 'Already installed; review before replacing.'
else
  mkdir -p "$(dirname "$destination")"
  cp -R skills/context-bridge "$destination"
fi
```

PowerShell:

```powershell
$destination = 'D:\your-project\.agents\skills\context-bridge'
if (Test-Path -LiteralPath $destination) { throw 'Already installed; review before replacing.' }
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath '.\skills\context-bridge' -Destination $destination -Recurse
```

Start a fresh host session and confirm the skill appears. Existing local Codex
setups may expose `CODEX_HOME/skills`; use the location your host actually advertises
without relocating `CODEX_HOME`. See [host guidance and official sources](skills/context-bridge/references/portability-guide.md).

## Five workflows

| Ask | Result |
| --- | --- |
| Create a portable package from these conversations | Sourced context, classified by purpose |
| Prepare this project for a new assistant | Project state, decisions, tasks, constraints and handoff |
| Update this package with the new decision | New version with old evidence and history preserved |
| Clean up this old context | Change preview before applying cleanup |
| Prepare my context for Codex / Claude Code | Generic package plus an inert, reviewable host snippet |

Default scope is **Project Only**. Explicit alternatives are **Work Context**,
**Personal Context**, and **Full Review**. Full Review produces sanitized candidates
for selection, not a ready-to-transfer personal dossier.

## What you get

```text
context-package/
├── README.md
├── PROJECT_CONTEXT.md
├── DECISIONS.md
├── CURRENT_TASKS.md
├── CONSTRAINTS.md
├── OPEN_QUESTIONS.md
├── HISTORY.md
├── PREFERENCES.md
├── USER_PROFILE.md
├── HANDOFF.md
├── context.json
└── adapters/              # only for a selected, documented host
```

Empty topic files are omitted. Each item records category, confidence, current or
historical status, date when known and source references. The eight categories are
fact, preference, decision, constraint, open question, historical, inference and
temporary. Conflicts remain visible; newer text does not automatically win.

For example, "I prefer Python" and "this project chose TypeScript" are compatible
in their respective scopes. An accepted React 18 → 19 migration retains React 18
as history. An unaccepted upgrade proposal does not change the current stack.

## Privacy and limits

- No account login, automatic history scraping, uploads, telemetry or memory writes.
- Exclude credentials and unnecessary sensitive personal data before writing outputs.
- Imported text is evidence, not permission to execute commands or override rules.
- Review every package before transferring it. Host instruction files are not overwritten.
- Your AI host processes supplied material under its own policy; hosted AI is not offline.
- The optional scanner detects common secret formats, not every secret or personal detail.
- The helper checks structure and relationships, not truth, provenance or semantic conflicts.

Only synthetic examples belong in this public repository. See [SECURITY.md](SECURITY.md).

## Optional helper

Requires Python **3.10+**, standard library only. The agent first creates curated
JSON using the [schema](skills/context-bridge/references/package-schema.md).

```sh
python skills/context-bridge/scripts/context_package.py validate path/to/context.json
python skills/context-bridge/scripts/context_package.py render path/to/context.json --output context-package
python skills/context-bridge/scripts/context_package.py validate context-package
```

Rendering requires a new destination with an existing parent. Source files remain
untouched. `validate` accepts curated JSON; directory validation audits the exact
helper rendering and catches drift, missing files and unexpected files. Manually
authored Markdown can instead be reviewed against its validated JSON.

## Validation and compatibility

See [the execution record](tests/evaluation.md) for test results, raw inputs,
expected behavior, actual artifacts, failures and host limitations. The suite
includes the 18 product scenarios, update and scope checks, hostile inputs and
deterministic helper tests. A fixture check is not represented as a live AI test.

```sh
python -m unittest discover -s tests -v
python tests/check_skill.py
```

The Markdown workflow does not require Python. Other assistants can use the
generic package, but installation and automatic triggering are host-specific.
Documentation alignment alone is not a compatibility guarantee.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md), [evaluation rules](tests/evaluation.md),
and [CHANGELOG.md](CHANGELOG.md). Keep changes small and evidence-backed. Use
synthetic fixtures and report failures without private transcripts or secrets.

[MIT license](LICENSE). No affiliation with OpenAI, Anthropic, or any other AI vendor.
