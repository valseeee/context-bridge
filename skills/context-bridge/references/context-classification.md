# Classification and evidence

Category answers **what kind of statement?** Area answers **where does it belong?**
Status answers **is it current?** Confidence answers **how well is it supported?**
Do not collapse these distinctions.

| Category | Use for | Common mistake |
| --- | --- | --- |
| `fact` | A sourced assertion about a project or person | Calling an assistant guess a fact |
| `preference` | An explicitly expressed way the user likes to work | Inferring a lifelong preference from one task |
| `decision` | An accepted choice, with rationale when known | Treating a proposal as accepted |
| `constraint` | A requirement, prohibition or actual limit | Omitting a constraint to save space |
| `open_question` | An unresolved choice or missing information | Inventing an answer |
| `historical` | An important past event or retired arrangement | Presenting it as current |
| `inference` | A useful conclusion not explicitly established | Using `verified` confidence |
| `temporary` | A short-lived arrangement or deadline | Making it a permanent preference |

Areas: `user`, `project`, `decision`, `task`, `constraint`. For example an explicit
"For Harbor, give me Chinese progress updates" is a project-scoped preference;
"I enjoy hiking" is personal user context and excluded from Project Only.

Use a stable subject, e.g. `project:harbor`, and a topic key, e.g. `frontend.version`.
Only compare claims with compatible subjects, topics and time periods. Preserve
qualifiers, exceptions, units, negative requirements and the speaker's intent.

Confidence:

- `verified`: directly supported by an authoritative source for this assertion,
  such as an accepted decision or an explicit preference from the user. This is
  source verification, not a guarantee of present-day truth.
- `reported`: a source claims it; it has not been independently established.
- `inferred`: a deduction; use category `inference` too.
- `uncertain`: ambiguous, disputed, or missing corroboration.

Statuses: `current`, `historical`, `stale`, `conflict`. Unknown dates are `null`.
An old date alone does not make a stable constraint stale. A dated deadline whose
period has elapsed is stale, but do not claim the task was completed or canceled.
An assistant suggestion remains an inference or open question unless the user
accepted it. In bilingual material preserve meaning and evidence across languages.
