# Project Scaffold Checklist

Use this checklist during a new project's first Codex thread. Complete the minimal section first; enable add-ons only when the project needs them.

## Minimal Profile

- [ ] Local Git repository exists and `.gitignore` excludes large/generated files.
- [ ] `README.md` states the project goal and next action.
- [ ] `PROJECT_INDEX.md` records known paths, current workstreams, and unknowns.
- [ ] `AGENTS.md` contains the project's working rules.
- [ ] `docs/definitions.md` and `docs/method_registry.md` exist.
- [ ] `docs/codex/analysis_contract_template.md` exists.
- [ ] `docs/codex/outputs_manifest.template.json` is available for formal analyses.
- [ ] Raw-data policy and the first minimal analysis are clear enough to proceed.

## Optional Add-ons

### Literature

Enable with `--profile full` when method design depends on papers:

- [ ] Seed references are provided or permission to search is recorded.
- [ ] `docs/literature/reference_manifest.csv` exists.
- [ ] Literature review and method-implication notes exist or are planned.

### Remote And Sbatch

Enable with `--profile full` when execution requires a server:

- [ ] Remote SSH alias and runtime/data/result paths are confirmed or marked unclear.
- [ ] `docs/codex/git_remote_workflow.md` is reviewed.
- [ ] `docs/codex/remote_sbatch_task_protocol.md` is reviewed.
- [ ] Inputs, outputs, logs, resources, runtime estimate, and mathematical method will be reviewed before submission.

## Before Implementation

- [ ] A task mode is chosen.
- [ ] The analysis contract is clear enough for the current task.
- [ ] Expected outputs and at least one validation check are named.
- [ ] Files and folders that must not be touched are recorded.
