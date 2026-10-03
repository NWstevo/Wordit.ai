# Commit Guide
# Contributing

Use this format for commit messages:

`type(scope): imperative summary`

Write the summary in lowercase, start with an action, and leave off the full stop. Add an issue number at the end when relevant, for example `(#42)`.

## Types

- `feat` — add new behaviour  
  Example: git commit -m `feat(auth): add password reset`
- `fix` — correct a defect  
  Example: git commit -m `fix(api): handle empty responses`
- `test` — add or update tests only  
  Example: git commit -m `test(auth): cover expired tokens`
- `refactor` — restructure code without changing behaviour  
  Example: git commit -m `refactor(api): simplify request parsing`
- `docs` — change documentation only  
  Example: git commit -m `docs(readme): clarify setup steps`
- `chore` — update tooling, configuration, or housekeeping  
  Example: git commit -m `chore(deps): update lint config`

Keep each commit to one logical change.