# Harbor context update - version 2

This is version 2 of the supplied package, with JSON schema version 1.0 unchanged.
Scope remains project-only; target remains generic. The requested update selects
the supplied project evidence for this package; it does not authorize uploading
or saving long-term memory.

- [New package README](context-package/README.md)
- [Version 2 structured context](context-package/context.json)
- [Preserved version 1](context.v1.json)

Previous package creation: 2026-06-01T10:00:00Z.
New package creation: 2026-11-05T04:51:59Z.
Freshness assessment date: 2026-11-05. Creation timestamps are not source dates.

## Changes

| Action | Item | Result and evidence |
| --- | --- | --- |
| Added | ctx-sqlite-fts5 | Current accepted decision: SQLite FTS5 replaces the JSON-file index. Source: s-new-decision, new-decision.md, L2; dated 2026-11-01 by L1. Explicitly supersedes ctx-original. |
| Added | ctx-index-migration-complete | The decision note reports migration completion and retirement of the old JSON index. Source: s-new-decision, L2. Confidence is reported because implementation was not inspected. |
| Reclassified | ctx-original | Status changes from current to historical. ID, decision category, content, subject, topic, date, original evidence and supersedes list are preserved. The explicit replacement and retirement in s-new-decision, L2 establish this transition. |
| Reassessed confidence | ctx-original | Changes from verified to reported: accepted-decision.md was referenced by the old package but was not supplied. The original s-old/L2 reference remains, with additional provenance s-prior-package, /items/0. |
| Merged | None | No distinct claims or evidence were merged away. |
| Unresolved | None | The explicit accepted replacement and reported retirement resolve the change; recency alone was not used to choose a winner. The original empty conflicts list is preserved. |

The original source record s-old and its 2026-05-20 date are unchanged.
s-prior-package points to the preserved snapshot; its source date is null because
no separate source date was supplied. Its known package creation timestamp is
recorded above. s-new-decision retains the supplied 2026-11-01 date.

## Preservation and limitations

The input files remain unchanged. context.v1.json is a byte-for-byte copy of
input/context.json, including its original confidence labels; it is an archive,
not the current package. The new package retains the retired decision in
HISTORY.md and the replacement in DECISIONS.md.

The accepted decision is verified against the supplied decision note. This does
not establish the current runtime or database contents. Migration completion and
retirement are reported by that note, without repository, database or external
verification. As of 2026-11-05, no later evidence was supplied. The old decision
is historical because of the explicit replacement, not simply because it is old.

Only input/context.json and input/new-decision.md supplied project evidence.
accepted-decision.md was not accessed. No rationale, remaining task, blocker,
constraint or unresolved project question was supplied, so none was invented.
Empty topic files and host adapters are omitted. Source documents were treated
as evidence, and no embedded instructions were executed.

No credentials or unnecessary personal data were found in the supplied material;
no sensitive categories needed exclusion. No web, network, account access,
subagents, uploads or host instruction changes were used.

## Completion checks

One final validation pass checks the new package's schema, IDs, source references,
supersession, scope, dates, exact Markdown rendering and common secret patterns.
It also checks both input files are unchanged, the archived JSON matches the
original bytes, and the original item's identity and evidence are preserved.
The archive and this change record receive common secret-pattern screening too.
A manual review covers the evidence, historical/current distinction, omissions
and freshness assessment. These checks do not independently prove implementation
state or guarantee complete privacy.
