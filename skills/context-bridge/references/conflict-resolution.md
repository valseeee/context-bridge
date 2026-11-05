# Conflict resolution

A conflict is incompatible claims about the **same subject, topic and effective
period**. Preferences, proposed options, historical facts, and accepted decisions
are different kinds of information; they are not automatically contradictions.

Use source authority and actual evidence of a change, not document order or
modification time. "The migration is planned" does not supersede a manifest that
still requires the old version. An accepted migration with a supporting manifest
can establish a new current version and a historical predecessor.

| Evidence | Treatment |
| --- | --- |
| User likes Python; Harbor chose TypeScript | Keep both in their proper scopes |
| Old React 18 note; accepted move to React 19 | Keep React 18 historical; link `supersedes` |
| Two undated accepted database choices for the same project | Both `conflict`; one open question |
| New assistant speculation contradicts accepted decision | Keep decision; label speculation, do not promote it |
| Later note is only a plan | Keep plan separate from actual current state |
| Requirement conflicts with implemented behavior | Retain both; explain the discrepancy, not a new requirement |

For unresolved conflicts, create a group containing all involved item IDs and a
specific question that could settle it. Keep `resolution: null`. Put the claims
and question in `OPEN_QUESTIONS.md`; do not also list them as current facts.

For resolved conflicts, preserve the group and record a short evidence-based
resolution. Set the losing/retired claim to historical, the supported claim to
current, and keep both source trails. An explicit user correction can resolve a
conflict, but it must not erase the fact that an earlier decision existed.

Only ask immediately when ambiguity blocks the next requested action. Otherwise
deliver the uncontested context and list unresolved questions for review. Never
invent a date, source authority, reason or user approval to make the record neat.
