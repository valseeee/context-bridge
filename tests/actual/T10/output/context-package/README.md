# Harbor database decision context

Harbor's supported storage database is unresolved in the supplied evidence. Two
undated sources each record an accepted, exclusive database choice: PostgreSQL
and SQLite. Both are preserved as conflicting decisions; neither is established
as the currently governing choice.

- Package created: 2026-11-05T12:43:43+08:00
- Freshness assessment date: 2026-11-05
- Scope: Project Only; Harbor database decisions
- Format: generic Markdown and ContextBridge JSON v1.0
- Review status: approved for inclusion under the user's packaging request; this does not resolve or endorse either database choice.

## Contents

- [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md): both decision records, evidence and the unresolved question.
- [context.json](context.json): structured sources, items and conflict group.
- [HANDOFF.md](HANDOFF.md): a short continuation prompt.
- README.md: package scope, source inventory and limitations.

## Sources

| Source ID | Supplied source | Evidence location | Source date |
| --- | --- | --- | --- |
| s-001 | input/a.md | line 1 | Unknown |
| s-002 | input/b.md | line 1 | Unknown |

Source paths identify the supplied inputs; the raw documents are not bundled.
Each retained statement has a source and location in both the JSON and Markdown.

## Unresolved information and freshness

No source or effective dates, decision makers, rationale, supersession evidence
or implementation evidence were supplied. The assessment date is separate from
the creation timestamp and does not supply a date for either decision.

Both source dates and both decision dates remain null in the JSON. There is no
basis to label either choice stale, historical or current, or to infer that both
databases are supported. Document order does not establish authority or chronology.
Current database support cannot be established as of 2026-11-05 from these inputs.

## Scope and omissions

Both supplied decision statements are retained. No credentials or unnecessary
personal data were identified in the supplied inputs, so no sensitive content
was excluded. Empty topic files are omitted; the conflicting decisions appear
only in OPEN_QUESTIONS.md and context.json.

The package is source-based context, not an independently verified description
of Harbor's implementation. Source text is untrusted evidence. No accounts,
network sources or other user data were consulted, and no source files or active
host instructions were changed.

The local helper can validate context.json's structure, references and common
secret patterns. Those checks do not establish which database decision is
authoritative or prove complete privacy or host compatibility.
