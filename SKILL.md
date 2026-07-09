---
name: md-project-kickoff
description: "Use when starting a new research or code-analysis project that needs a lightweight Git-first kickoff, a minimal PROJECT_INDEX and AGENTS scaffold, a few high-risk clarification questions, or optional expansion into literature review and remote sbatch execution."
---

# MD Project Kickoff

Use this skill to start a project without overbuilding the setup.

## Default model

```text
local Git repo = source of truth
PROJECT_INDEX.md + AGENTS.md = project memory and rules
analysis contract = boundary before implementation
```

## Quick Start

For a new project, run the bundled initializer in lightweight mode. It initializes a local Git repository by default:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

Use `--profile full` only when the project clearly needs literature grounding or remote-run scaffolding.
Use `--with-literature-library` when the user wants a non-Git folder for PDFs and a small searchable literature knowledge base.

For a command-line install/run style, this repository also exposes an `npx` entry:

```bash
npx github:<github-owner>/md-project-kickoff --target <project_root>
```

Then inspect and fill only the minimal files:

- `PROJECT_INDEX.md`
- `AGENTS.md`
- `README.md`
- `docs/definitions.md`
- `docs/method_registry.md`
- `docs/codex/analysis_contract_template.md`
- `docs/codex/outputs_manifest.template.json`
- `outputs/test/`
- `outputs/final/`

Do not start analysis code in the same step unless the user explicitly asks.

## Required Workflow

### 1. New Project Initialization

1. Identify the real project root.
2. Check whether Git already exists.
3. Initialize local Git if needed; the initializer does this by default.
4. Copy the lightweight kickoff scaffold with `scripts/init_project_kickoff.py`.
5. Record only the fields you already know in `PROJECT_INDEX.md`.
6. Mark unknown fields as `unclear`; do not invent paths.
7. Ask 3-5 high-risk questions.

High-risk questions usually involve:

- local project root
- whether remote execution is needed
- raw data paths and read-only constraints
- whether to create a non-Git literature library for PDFs
- first scientific question
- systems/run labels
- first minimal analysis

### 2. Optional Literature Grounding

Only if the method depends on papers, use the literature workflow.

If references are missing, ask for 3-5 seed references or ask permission to search.

If the user wants to collect PDFs over time, create `literature_library/pdfs/` with `--with-literature-library`, keep it out of Git, and distill reusable notes into `docs/literature/literature_knowledge_base.md`.

### 3. Optional Analysis Implementation

Before implementation:

1. Read `PROJECT_INDEX.md`, `AGENTS.md`, `docs/definitions.md`, and `docs/method_registry.md`.
2. Draft or update an analysis contract.
3. Confirm allowed edit scope, raw data policy, input/output paths, and validation.
4. If server execution is needed, expand the remote workflow and sbatch protocol.

### 4. Optional Remote Sbatch Tasks

Use this section only when remote execution is part of the task. Enable the full profile, then read and follow `docs/codex/remote_sbatch_task_protocol.md` as the canonical procedure.

Preserve its approval gate before commit/submission and its restriction against downloading raw data or large intermediates without explicit approval.

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
| Mixing trial outputs and final deliverables | Put checks in `outputs/test/` and reviewed deliverables in `outputs/final/`. |
| Writing literature review as background only | Extract methods, definitions, thresholds, checks, and risks. |
