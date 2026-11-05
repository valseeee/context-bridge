# Harbor decision

## ctx-001: Use SQLite

The user confirmed SQLite for Harbor because the tool must work offline without a database server.

- Category: decision | Area: decision | Scope: project
- Subject: project:harbor | Topic: storage.database
- Status: current | Confidence: verified | Sensitivity: normal
- Date: 2026-10-20 (source confirmation date)
- Evidence: src-001, input/decision.md, line 2, User; source date in line 1
- Supersedes: none recorded

The governing requirement is preserved separately as ctx-002 in [CONSTRAINTS.md](CONSTRAINTS.md). This records an accepted choice; it does not establish that SQLite has been implemented.
