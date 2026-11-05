# Harbor constraint

## ctx-002: Offline operation without a database server

Harbor must work offline without a database server.

- Category: constraint | Area: constraint | Scope: project
- Subject: project:harbor | Topic: runtime.offline
- Status: current | Confidence: verified | Sensitivity: normal
- Date: 2026-10-20 (source statement date)
- Evidence: src-001, input/decision.md, line 2, User; source date in line 1
- Supersedes: none recorded

This requirement is the stated reason for the SQLite choice in [DECISIONS.md](DECISIONS.md). No implementation or verification results were supplied.
