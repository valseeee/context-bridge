# Preferences example

Selected scope: Work Context.

Input, source `pasted-1`, date unknown:

> User: For work, I prefer brief Chinese progress updates.
> User: Please keep work updates short and in Chinese.
> Assistant: You probably prefer Python to every other language.

Merge the two explicit preferences, keeping both message locations. They become
one work-scoped preference. The assistant's guess is not a confirmed preference;
omit it if irrelevant or label it as an inference with inferred confidence.
For Project Only, exclude a generic user profile unless the user makes the
preference specific to the selected project.
