---
name: md-project-kickoff
description: "Use when starting or restructuring a research or code-analysis project that needs a lightweight Git-first kickoff, persistent project memory, high-risk clarification questions, literature grounding, or a local-to-SSH Slurm workflow."
---

# MD Project Kickoff

Use this Agent Skills-compatible workflow to start a project without overbuilding
the setup. The project files are the shared source of truth; the host Agent only
changes how this workflow is discovered and invoked.

## Default model

```text
local Git repo = source of truth
PROJECT_INDEX.md + AGENTS.md = project memory and shared rules
analysis contract = boundary before implementation
```

Host entry points:

- Codex: `$md-project-kickoff`
- Claude Code: `/md-project-kickoff`
- Cursor: `/md-project-kickoff` or the direct initializer command

`agents/openai.yaml` is optional Codex UI metadata. It is not required by the
shared workflow.

## Quick Start

For a one-command installation, use the bundled cross-platform installer:

```powershell
irm https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.ps1 | iex
```

```bash
curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash
```

The installer requires Node.js 18+, detects Codex/Claude Code/Cursor and the
generic Agent Skills directory, and can be forced to all targets with `--all`.
It is safe to rerun for updates.

For a new project, run the bundled initializer in lightweight mode. It initializes a local Git repository by default:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

Use `--profile full` only when the project clearly needs literature grounding or remote-run scaffolding.
Use `--with-literature-library` when the user wants a non-Git folder for PDFs and a small searchable literature knowledge base.
Use `--agent claude`, `--agent cursor`, or `--agent all` when the project should also receive host-specific instruction entry points.

For a host-independent command-line install/run style, this repository also exposes an `npx` entry:

```bash
npx github:<github-owner>/md-project-kickoff --target <project_root>
```

Then inspect and fill only the minimal files:

- `PROJECT_INDEX.md`
- `AGENTS.md`
- `README.md`
- `docs/definitions.md`
- `docs/method_registry.md`
- `docs/codex/analysis_contract_template.md` (legacy-compatible workflow path)
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
8. If the project has a local-plus-SSH workflow, record both endpoints and the sync policy before submitting any batch job.

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

The following are non-negotiable for every new Slurm workflow:

- `.out` states the task, system/run, selected inputs, parameters, output root, start time, end time, and exit status.
- `.err` carries unbuffered, promptly flushed `tqdm`-style frame progress, warnings, and diagnostics.
- Array tasks have distinct logs and record task ID, system/run, and output directory.
- Aggregation tasks record dependency jobs, input result root, and output files.
- A smoke test runs before a large submission and verifies useful information in both `.out` and `.err`.

For the complete procedure, read `docs/codex/remote_sbatch_task_protocol.md`.

Remote boundary:

- Edit, test, commit, and push from the local checkout only.
- Use the SSH server for code update, execution, and large-result storage.
- Compare local/server commit IDs, branches, and tracked file state before running.
- Copy back only selected small summaries, figures, and manifests.
- Never silently delete or overwrite files; propose cleanup and wait for approval.

## Bundled Resources

- `assets/md-project-kickoff-template/`: source templates and prompts.
- `scripts/init_project_kickoff.py`: copies scaffold files into a project.
- `bin/install.js`, `install.sh`, `install.ps1`: cross-platform skill installer.

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
