# Public skills repository

IMPORTANT: Everything in this repo is public-facing, so do not place any sensitive info here and make sure to distinguish between what should be internal-facing info (e.g. secrets, PII, recording guides/scripts), and public-facing info (instructions, how-to guides, actual code utilized). If there is information the assistant needs across sessions but should not be published, put it in the `.internal/` folder which is ignored by git per the `.gitignore`.

The portable skills in `skills/<name>/` are maintained here. Categories and external suites live in `catalog/skills.json`. Each installed skill must work independently of this checkout, including its scripts and references. Preserve its existing invocation name.

Keep large application and plugin suites in their own source repositories. Link them through the catalog and marketplace. Do not copy private skills or third-party skills into the authored collection.

Before changing a migrated skill, read its provenance in `catalog/provenance.json`. Record intentional changes there. Add related public tutorials to `docs/videos.md`; production notes and full internal transcripts stay private.

For caption retrieval, use a transcript downloader or existing transcript artifacts. Reserve vidIQ for keyword optimization, video packaging, and briefing.

Run `python3 scripts/check_catalog.py` and `python3 -m unittest discover -s tests` before publishing changes. The installer must refuse to overwrite existing skills. Do not install to real user skill folders during tests.

