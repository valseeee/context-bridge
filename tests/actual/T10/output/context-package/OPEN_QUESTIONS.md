# Harbor database decision conflict

The supplied sources make incompatible exclusive choices for the same project
and topic. Both call their choice accepted, but neither supplies a date or
evidence that it supersedes the other. Their effective periods are unknown.
The governing choice remains unresolved.

## ctx-001

The source records an accepted Harbor decision: PostgreSQL is the only supported storage database.

- Category: decision | Area: decision | Scope: project
- Subject: project:harbor | Topic: storage.database
- Status: conflict | Confidence: uncertain
- Effective date: unknown (null)
- Evidence: s-001, input/a.md, line 1; source date unknown (null)
- Sensitivity: normal | Supersedes: none

## ctx-002

The source records an accepted Harbor decision: SQLite is the only supported storage database.

- Category: decision | Area: decision | Scope: project
- Subject: project:harbor | Topic: storage.database
- Status: conflict | Confidence: uncertain
- Effective date: unknown (null)
- Evidence: s-002, input/b.md, line 1; source date unknown (null)
- Sensitivity: normal | Supersedes: none

Confidence is uncertain because the governing decision is disputed. Each source
explicitly labels its own choice accepted; that wording alone does not establish
its authority or present applicability.

## conf-001

Which accepted decision governs Harbor's only supported storage database (PostgreSQL or SQLite), and what authoritative decision record or explicit owner confirmation establishes it?

- Members: ctx-001, ctx-002
- Resolution: unresolved (null)
- Freshness assessment date: 2026-11-05; neither decision's current applicability is established.

No decision maker, rationale, effective date, replacement relationship or
implementation evidence is available in the inputs. Preserve both claims and
their provenance until a sourced resolution is supplied. Any later resolution
should record its evidence and retain the earlier records.
