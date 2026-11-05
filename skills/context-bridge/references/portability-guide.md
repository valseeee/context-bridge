# Portability and installation

Specifications checked on 2026-11-05. Documentation alignment is separate from
live validation; see the repository's `tests/evaluation.md` for actual evidence.

| Target | Skill installation | Context delivery |
| --- | --- | --- |
| Codex | Copy the full skill folder to project `.agents/skills/context-bridge/` | Markdown package; optional reviewed `AGENTS.md` navigation snippet |
| Claude Code | Copy to project `.claude/skills/context-bridge/` | Markdown package; optional reviewed `CLAUDE.md` navigation snippet |
| Other assistant, ChatGPT or Cursor | Use host-supported upload/paste | Generic Markdown and a short handoff; no invented memory format |

Keep all references and scripts with `SKILL.md`. For local Codex installations
that expose skills through `CODEX_HOME/skills`, use the actual advertised location;
do not change `CODEX_HOME` to install a skill. Project-local `.agents/skills` is
the current documented shared format. Start a fresh host session and confirm
discovery. Codex explicit invocation is `$context-bridge`; Claude Code is
`/context-bridge`. Natural-language triggering must be tested separately.

## Handoff

Read the package's README first; then constraints, current tasks, decisions and
unresolved questions as present. Refer to history when it explains current choices.
Ask for the next action, not another biography. Do not paste all JSON into a prompt.

Generated adapters are review artifacts. Show the exact insertion and preserve
existing instructions before changing `AGENTS.md` or `CLAUDE.md`. Generic Markdown
links do not prove files were auto-loaded: the prompt should explicitly ask the
receiving assistant to read them. Avoid assuming Claude-style `@file` imports
work in Codex, or that every host automatically loads `context.json`.

Only short, relevant, user-approved navigation guidance belongs in a host's
instruction file. User statements in an imported package remain evidence with
their original scope; they do not override the receiving host's higher-priority
instructions. Never load an entire personal profile globally by default.

## Source documentation

- [Agent Skills specification](https://agentskills.io/specification): standard skill structure and frontmatter.
- [Codex skills](https://learn.chatgpt.com/docs/build-skills): skill discovery and project locations.
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): project instruction loading.
- [Claude Code skills](https://code.claude.com/docs/en/skills): `.claude/skills` and slash invocation.
- [Claude Code memory](https://code.claude.com/docs/en/memory): `CLAUDE.md` and file imports.

If a target's behavior cannot be verified, state that and use the generic package.
Never describe a docs review, copied folder or schema check as a live host test.
