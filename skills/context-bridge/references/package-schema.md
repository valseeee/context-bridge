# Package contract v1.0

Use [context.schema.json](context.schema.json) for the machine-readable contract.
The optional `scripts/context_package.py` checks this contract plus ID relations,
scope, date validity and common secret patterns. It does not prove provenance or
understand whether two natural-language claims conflict; the agent must do that.

## JSON

Top level: `schema_version` (`1.0`), `generated_at` (ISO 8601 timestamp with timezone),
`scope` (`project-only`, `work`, `personal`, `full-review`), `target` (`generic`,
`codex`, `claude-code`), `review_status` (`candidate`, `approved`), `sources`,
`items`, `conflicts`. `approved` means selected for this package, not uploaded or
approved for long-term memory. Ordinary Create/Handoff requests authorize their
specified scope; they do not require another generic approval question.

Sources contain `id`, a safe `label`, `kind` (`file`, `pasted`, `conversation`),
and `date` (a supplied `YYYY-MM-DD` or `null`). Use a label such as `pasted-1` for
pasted text. Source dates must never be replaced by the package creation date.

Every item contains:

| Field | Meaning |
| --- | --- |
| `id` | Stable unique ID, e.g. `ctx-001` |
| `category` | One of the eight classification types |
| `area` | `user`, `project`, `decision`, `task`, `constraint` |
| `scope` | `project`, `work` or `personal` relevance |
| `subject` | Specific entity, e.g. `project:harbor` |
| `key` | Topic within the subject, e.g. `frontend.version` |
| `content` | One useful, self-contained, sanitized statement |
| `status` | `current`, `historical`, `stale`, `conflict` |
| `confidence` | `verified`, `reported`, `inferred`, `uncertain` |
| `evidence` | Nonempty array of `{source_id, locator}`; locator can be null |
| `date` | Supplied effective date, or null if unknown |
| `sensitivity` | `normal`, `sensitive` or `credential`; portable entries must be normal |
| `supersedes` | IDs of preserved historical predecessors; empty array normally |

Do not silently coerce strings, drop unknown fields or duplicate IDs. All listed
fields are required, and additional fields are not part of this version.
Inference category and confidence must agree. Historical category cannot be
current. Project Only accepts only project-scoped entries. Work accepts project
and work entries. A personal statement does not become project context just by
changing its scope field; relevance needs semantic review.

Conflicts contain `id`, `item_ids` (at least two), `question`, `resolution` (null
for unresolved, otherwise a sourced explanation). Each unresolved member must
have conflict status, and every conflict-status item needs an unresolved group.
Resolved groups may remain in JSON as history. Superseded items remain present
as historical; supersession cannot be self-referential or cyclic.

## Files

Always: `README.md`, `context.json`, `HANDOFF.md`.

| File | Items |
| --- | --- |
| `USER_PROFILE.md` | Relevant user-area background |
| `PREFERENCES.md` | Explicit preferences |
| `PROJECT_CONTEXT.md` | Project facts and labelled inferences |
| `DECISIONS.md` | Accepted decisions and rationale |
| `CURRENT_TASKS.md` | Task-area next steps and blockers |
| `CONSTRAINTS.md` | Requirements and prohibitions |
| `OPEN_QUESTIONS.md` | Open questions and unresolved conflicts |
| `HISTORY.md` | Historical/stale items and resolved conflict explanations |

History/conflict status takes priority over topical routing. Omit empty topic
files; never fabricate content to fill them. Each rendered item carries its ID,
category, confidence, status, date and source references. README records scope,
creation time, actual contents and limitations. HANDOFF is short and references
only files that exist. Candidate output is not labelled ready for transfer.

For Codex or Claude Code, `adapters/codex.md` or `adapters/claude-code.md` contains
an inert snippet and application instructions. It does not create or replace the
host's active instruction file. Keep JSON, Markdown and the handoff consistent.

The helper reads UTF-8 (including a BOM), rejects duplicate JSON keys and writes
UTF-8. It refuses a destination that already exists. Use a new version directory
for updates; raw input files are never deleted or changed. Empty inputs require
clarification rather than an empty package. If file tools are unavailable, provide
the equivalent named file contents for the user to save manually.
