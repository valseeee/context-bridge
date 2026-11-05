# Retained failed attempts and scorer corrections

## T01, first attempt — environment failure

Started 2026-11-05T04:21:58.275831+00:00; duration 87.32 seconds.
Codex CLI process exit code: 0. Scenario outcome: **FAIL**.

Actual final response:

> Blocked by the local runtime: file-access tools fail with `registered Core launch requires an installed app`.
>
> I couldn’t read `input/notes.md` or the context-bridge skill, so no package was created. Restore local execution and retry to generate `output/context-package`.

The completed command events had exit code -1 and no successful source/skill
read. The original observer mistakenly treated SKILL.md appearing in an attempted
command as a successful read; that observer was corrected to require completion
and actual Skill content. The desktop's injected runtime registration variables
were removed only from independently launched test children. Global configuration
and the active CODEX_HOME were not changed.

Raw trace SHA-256:
`de165d270edbdaa7dda9abd34bd108ccdb758986307d2128e1c3e725ff6d011d`.
The successful retry and artifacts are under [actual/T01](actual/T01/response.md).

## T17 — scorer false negative

The actual response clearly requested that the user **place conversation exports**
under input/. No package was fabricated. The scorer's initial vocabulary included
provide/paste/share/attach but omitted place. It was corrected after reading the
actual response; no Skill behavior change or new model execution was needed.
See [the preserved actual response](actual/T17/response.md).

## Global discovery — probe false negative

The first dry-run probe searched for a fully expanded path. Codex advertised the
Skill with `r0/context-bridge/SKILL.md` and a separate root mapping. Parsing that
entry and mapping confirmed discovery. A catalog check does not by itself prove
invocation; the live workflow cases provide that evidence.

## Python 3.10 — timestamp precision compatibility

The first CI matrix passed, but review of T02's actual output found a timestamp
with seven fractional digits. Python 3.10's
[parser](https://github.com/python/cpython/blob/v3.10.16/Modules/_datetimemodule.c#L705-L718)
accepts only three or six. The helper now normalizes the value only for parsing,
preserving the original timestamp in exported JSON. Regression coverage checks
fractional precision and all recorded context JSON files on both supported CI
Python versions. Invalid timezone offsets are rejected explicitly.
