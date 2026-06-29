---
name: md-project-kickoff
description: Use when starting a new research/code analysis project, initializing PROJECT_INDEX.md or AGENTS.md, setting up Git-first local/remote workflows, planning remote sbatch runs, or grounding a project in literature before implementation.
---

# MD Project Kickoff

Use this skill to initialize or repair a project operating system for Codex-driven research work.

Core model:

```text
local Git repo = source of truth
remote server checkout = runtime container
PROJECT_INDEX.md + AGENTS.md = persistent project memory and rules
analysis contract = boundary before implementation
outputs_manifest.json = record of useful results
```

## Quick Start

For a new project, run the bundled initializer:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

Then inspect and fill:

- `PROJECT_INDEX.md`
- `AGENTS.md`
- `docs/definitions.md`
- `docs/method_registry.md`
- `docs/literature/reference_manifest.csv`
- `docs/codex/analysis_contract_template.md`

Do not start analysis code in the same step unless the user explicitly asks.

## Required Workflow

### 1. New Project Initialization

1. Identify the real project root.
2. Check whether Git already exists.
3. Initialize local Git if needed.
4. Copy the kickoff scaffold with `scripts/init_project_kickoff.py`.
5. Record local branch, remote SSH alias, remote bare repo, remote runtime checkout, remote data root, and remote results root in `PROJECT_INDEX.md`.
6. Mark unknown fields as `unclear`; do not invent paths.
7. Ask at most 7 high-risk questions.

High-risk questions:

- local project root
- remote SSH alias and runtime paths
- raw data paths and read-only constraints
- first scientific question
- systems/run labels
- seed references for literature grounding
- first minimal analysis

### 2. Literature Grounding

Before designing a method that depends on papers, use the scaffolded literature workflow.

Produce or update:

- `docs/literature/reference_manifest.csv`
- `docs/literature/literature_review.md`
- `docs/literature/method_implications.md`

Then update:

- `docs/definitions.md` for confirmed definitions, thresholds, windows, units, and assumptions.
- `docs/method_registry.md` for method candidates, canonical methods, methods to avoid, and validation checks.

If papers are missing, ask for 3-8 seed references or ask permission to search.

### 3. Analysis Implementation

Before implementation:

1. Read `PROJECT_INDEX.md`, `AGENTS.md`, `docs/definitions.md`, and `docs/method_registry.md`.
2. Draft or update an analysis contract.
3. Confirm allowed edit scope, raw data policy, input/output paths, and validation.
4. If server execution is needed, read `docs/codex/remote_sbatch_task_protocol.md`.

### 4. Remote Sbatch Tasks

Follow the three-stage protocol:

1. **Local review package**: edit code locally, check correctness, write `sbatch`, and show the user input paths, raw trajectory paths, output paths, log path, sbatch command, resource estimate, runtime estimate, and key math/statistics.
2. **After user approval**: commit, push, SSH to server, verify remote code is current, submit `sbatch`, and report job id/log/output paths/estimated finish time.
3. **After user reports completion**: SSH back, inspect logs/results, download only key lightweight results to the current thread `outputs/<analysis_id>/`, analyze results, and recommend next steps.

Do not download raw trajectories or large intermediates without explicit approval.

## Bundled Resources

- `assets/md-project-kickoff-template/`: source templates and prompts.
- `scripts/init_project_kickoff.py`: copies scaffold files into a project.

Important template files inside the asset:

- `AGENTS.template.md`
- `PROJECT_INDEX.template.md`
- `.gitignore.template`
- `docs/codex/git_remote_workflow.md`
- `docs/codex/remote_sbatch_task_protocol.md`
- `docs/codex/literature_review_workflow.md`
- `prompts/first_thread_prompt.md`
- `prompts/implement_verify_prompt.md`
- `prompts/literature_review_prompt.md`

## Common Mistakes

| Mistake | Correction |
|---|---|
| Starting code before Git/project rules exist | Initialize Git and scaffold first. |
| Treating the remote server as the source of truth | Local Git is the source of truth; remote is runtime. |
| Guessing remote paths | Mark unknown fields and ask. |
| Submitting sbatch before user reviews paths/math | Prepare review package first. |
| Downloading whole result folders | Use `outputs_manifest.json`; download only key lightweight outputs. |
| Writing literature review as background only | Extract methods, definitions, thresholds, checks, and risks. |
