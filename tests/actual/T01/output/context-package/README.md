# Harbor context package

Portable, project-only context for another AI, distilled from `input/notes.md` (source `s1`). This package contains five reported statements and uses generic Markdown plus structured JSON.

Generated: 2026-11-05T12:27:04+08:00
Freshness assessment date: 2026-11-05.

## Contents and use

Transfer this entire directory. Start the receiving AI with [HANDOFF.md](HANDOFF.md).

- [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md): purpose and reported technology stack.
- [CONSTRAINTS.md](CONSTRAINTS.md): requirement to work without a hosted database.
- [CURRENT_TASKS.md](CURRENT_TASKS.md): recorded next task, incremental indexing.
- [context.json](context.json): classified entries with stable IDs and line-level evidence references.

## Evidence and freshness

Source `s1` is the supplied English note titled Harbor. Its author and date are not supplied. All source and item dates remain `null`; the package creation timestamp does not date the underlying claims.

Every entry has `reported` confidence. `current` means retained as the source's latest available context, not independently verified project state on 2026-11-05. With no source dates, freshness cannot be established; there is no evidence to classify an entry as expired or superseded. The receiving AI should verify the runtime, storage implementation and task status against authorized current project material before implementation.

## Missing context and limits

No repository, source code, commands, tests, implementation progress, or detailed incremental-indexing requirements were supplied. No accepted design decisions or decision rationale were recorded. In particular, how incremental indexing should handle added, changed and removed documents remains unspecified; this is a handoff question, not an established requirement.

No contradictory claims were found in the supplied note. No open decisions, historical events or personal preferences have been invented to fill topic files. Missing implementation material limits coding, but does not prevent transferring the supplied context.

All substantive project statements in the note are retained. The raw source is not bundled; the relative source label and line locations record provenance, and the distilled context can be read without the original file. No credentials or unnecessary personal data were identified. Empty topic files and host-specific adapters are omitted. No account access, upload, long-term memory change or host instruction change is part of this package.

The structured JSON can be checked with the local ContextBridge validator. Structural and common secret-pattern checks do not establish present-day truth, complete privacy or compatibility with a particular AI host.
