# Project Scaffold Checklist

Use this checklist during a new project's first Codex thread.

## Required Files

- [ ] `PROJECT_INDEX.md`
- [ ] `AGENTS.md`
- [ ] `README.md`
- [ ] `.gitignore`
- [ ] `docs/definitions.md`
- [ ] `docs/method_registry.md`
- [ ] `docs/literature/reference_manifest.csv`
- [ ] `docs/literature/literature_review.md` or placeholder
- [ ] `docs/literature/method_implications.md` or placeholder
- [ ] `docs/codex/analysis_contract_template.md`
- [ ] `docs/codex/git_remote_workflow.md`
- [ ] `docs/codex/literature_review_workflow.md`
- [ ] `docs/codex/remote_sbatch_task_protocol.md`
- [ ] `docs/codex/output_manifest_schema.md`
- [ ] `docs/codex/migration_checklist.md`

## Recommended Folders

- [ ] `configs/`
- [ ] `scripts/`
- [ ] `src/`
- [ ] `tests/`
- [ ] `notebooks/exploratory/`
- [ ] `notebooks/summaries/`
- [ ] `docs/literature/`
- [ ] `results/`
- [ ] `logs/`
- [ ] `review/`

## First Questions To Clarify

- [ ] Where is the local project root?
- [ ] Should a new local Git repo be initialized?
- [ ] What is the remote SSH alias?
- [ ] What are the remote bare repo, runtime checkout, data root, and results root?
- [ ] What is the project's main scientific question?
- [ ] Where are the raw data and which files must not be touched?
- [ ] What are the systems/run labels?
- [ ] What seed references should guide method design?
- [ ] What definitions are already known?
- [ ] What definitions are not yet known?
- [ ] What is the first minimal analysis?
- [ ] What result would count as a useful first milestone?

## First Implementation Should Not Start Until

- [ ] Local Git status is known.
- [ ] `.gitignore` excludes large/generated files.
- [ ] Remote runtime path is recorded, or marked unclear.
- [ ] Literature seed references are recorded, or marked needed.
- [ ] If server execution is needed, sbatch review protocol is understood.
- [ ] A task mode is chosen.
- [ ] An analysis contract exists or Codex has drafted one.
- [ ] Raw data policy is clear.
- [ ] Expected outputs are named.
- [ ] A lightweight verification plan exists.
