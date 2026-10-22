# Contributing

Add a portable skill under `skills/<name>/`. Its folder name and frontmatter `name` must match. Put substantial supporting material in its own `references/`, `assets/`, or `scripts/` directory and link it from `SKILL.md` where needed.

Add the skill to `catalog/skills.json`, using an existing category when it fits. Record imported material and intentional changes in `catalog/provenance.json`. Keep attribution when adapting another author's work; externally maintained collections belong in the linked catalog unless their migration is explicitly agreed.

Avoid dependencies on files outside the installed skill folder. Use configurable paths instead of personal machine paths. State what the skill actually needs: a reviewer CLI, a GitHub connection, or a tracker integration.

Run these checks before opening a pull request:

```bash
python3 scripts/check_catalog.py
python3 -m unittest discover -s tests
```

Do not include account credentials, real meeting transcripts, client context, or local working notes. Put local-only material in `.internal/` and verify it is excluded from the proposed commit.

