# Project facts example

Input `README.md`, no source date:

> Harbor is a documentation search tool. The CLI uses Python 3.11 and SQLite.
> It must work without a hosted database. Next: add incremental indexing.

Extract project goal and stack as sourced facts, the no-hosted-database rule as a
constraint, and incremental indexing as a task. Dates remain null. Generate
PROJECT_CONTEXT, CONSTRAINTS and CURRENT_TASKS alongside README, JSON and HANDOFF;
do not invent USER_PROFILE or a project deadline. Preserve Python's exact version.
