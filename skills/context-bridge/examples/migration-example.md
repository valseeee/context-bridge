# Migration and update example

Existing sourced decision: "Harbor uses React 18", dated 2026-05-01.
New accepted decision: "The React 19 migration is complete", dated 2026-10-30,
supported by a supplied updated manifest.

Keep the old item ID as historical. Add the new current decision with its evidence
and `supersedes: [old-id]`. Preserve the original source date and new effective
date separately. Write a new package version beside the old one.

If the new note merely said "We might upgrade to React 19", retain React 18 as
current and classify the upgrade as a proposal/open question. If two accepted
decisions disagree and neither establishes a change, record a conflict instead.

For Claude Code, deliver Markdown plus an inert `CLAUDE.md` navigation snippet.
For an unknown host, keep Markdown and say the host-specific format is unverified.
Never silently replace the project's existing host instructions.
