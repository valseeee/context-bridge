# Harbor context — cleanup preview

Preview only; no cleanup has been applied. The source is unchanged. This is a proposal for review, not a ready-to-use context package.

- Scope: Harbor project only.
- Freshness assessment date: 2026-11-05.
- Source S1: `input/old-package.md`. Its document date is unknown (`null`).
- Confidence: the statements below are reported by S1, not independently verified as current.

## Proposed changes

| Source item IDs | Action | Proposed treatment and retained meaning | Evidence | Reason |
| --- | --- | --- | --- | --- |
| `ctx-001`, `ctx-002` | merge | Keep `ctx-001`: “Harbor uses SQLite.” Merge the duplicate `ctx-002` into it, preserving the old ID mapping and both evidence references. | S1, lines 2–3 | Identical claims about the same project. This removes repetition without establishing that SQLite is still in use today. |
| `ctx-003` | mark stale | Keep as a temporary item with stale status: “The temporary demo deadline was 2026-05-01; its outcome is unknown.” | S1, line 4 | The deadline predates 2026-11-05. Remove it from current-deadline context, but retain it for history. Elapsed time does not establish completion or cancellation. |
| `ctx-004` | retain | Preserve the constraint exactly: “Never delete original documents.” | S1, line 5 | This is an explicit prohibition with no supplied expiry or replacement. Its age does not make it stale. |

## Removals and retention

The only proposed removal is `ctx-002` as a standalone duplicate. Preserve the trace `ctx-002 → ctx-001` and references to both original lines; this is a merge, not evidence of a changed database decision. No unique information is proposed for deletion.

Retain the SQLite claim, the elapsed deadline and its unknown outcome, and the document-preservation constraint. Do not delete or rewrite the original source.

## Conflicts and uncertainty

No conflicting claims appear in the supplied file. Harbor’s current database and the demo outcome remain unverified. Those uncertainties do not block this preview; they would need fresh evidence before being presented as confirmed current state.

Keep unknown source and statement dates as `null`. The supplied 2026-05-01 is a deadline date, not a document creation date; 2026-11-05 is only the freshness assessment date.

## Review checks

Manual review accounted for all four source IDs and checked the proposed changes against their source lines, scope, freshness, and privacy. No credentials or unrelated personal data were identified for exclusion. The package validator is not applicable to this standalone Markdown preview. No external verification was performed.
