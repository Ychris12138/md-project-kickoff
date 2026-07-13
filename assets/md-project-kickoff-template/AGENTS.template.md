# AGENTS.md

This file defines how an AI coding or research agent should work inside this project.

## Core Rules

1. Read `PROJECT_INDEX.md` before doing project work.
2. Treat the local Git repository as the source of truth unless the user says otherwise.
3. Read `docs/definitions.md` and `docs/method_registry.md` only when the task touches scientific definitions or methods.
4. Treat the remote server path as a runtime container only when remote work is actually needed.
5. Do not inspect large raw data, trajectory, result, cache, or temporary folders unless the task requires it.
6. Do not move, delete, overwrite, or download raw data unless explicitly approved.
7. Prefer existing project conventions over inventing new layouts.
8. If a definition is unclear, ask the user instead of guessing.
9. Keep trial outputs and final deliverables separate: use `outputs/test/` for checks and `outputs/final/` for reviewed deliverables unless `PROJECT_INDEX.md` defines a stricter path.

## Local Development And SSH Boundary

These rules apply whenever the project has a local checkout and an SSH runtime:

1. The local checkout is the only development, editing, testing, and commit path.
2. The SSH server receives reviewed commits, updates its runtime checkout, runs jobs, and stores large results.
3. Server-side source changes must follow `local edit -> local test -> local commit -> push -> server update -> run`.
4. At project start, record the local path, SSH alias/path, Git branch, remote branch relationship, test directory, formal result directory, raw-data roots, and sync policy in `PROJECT_INDEX.md`.
5. Before a remote run, compare local/server commit IDs, branches, and tracked file state.
6. Copy back only selected small summaries, figures, manifests, and other explicitly requested review artifacts.
7. Never silently delete or overwrite files. List stale scripts, tests, logs, or intermediates as cleanup suggestions and wait for approval.

## Git And Remote Runtime

Use this section only when the project needs Git or remote execution.

1. Ensure the local project is a Git repository.
2. Ensure `.gitignore` excludes large raw data, generated results, logs, caches, virtual environments, and temporary folders.
3. Make an initial local commit containing only project structure and lightweight documentation.
4. Record remote SSH alias, remote runtime checkout, remote data root, and remote results root only if they are known.
5. Prefer this topology:

```text
local repo -> remote bare repo -> remote runtime checkout
```

Do not push directly into a checked-out non-bare remote working tree unless the user has explicitly configured and approved that workflow.

Standard remote run flow, when needed:

```text
local commit
git push <runtime_remote> <branch>
ssh <remote_alias> "cd <remote_runtime_checkout> && git pull --ff-only"
ssh <remote_alias> "cd <remote_runtime_checkout> && <run command>"
```

Remote inspection is allowed when the user has provided the SSH alias/path:

```bash
ssh <remote_alias>
cd <remote_runtime_checkout>
git status --short --branch
```

When remote commands may be long-running or destructive, ask first.

## Remote Sbatch Tasks

Use this section only for server-side analysis tasks.

When the full profile is enabled, read and follow `docs/codex/remote_sbatch_task_protocol.md` as the canonical three-stage procedure. It defines the local review package, approval gate, remote update and submission checks, completion handling, selective result download, and required reporting.

Always preserve these two constraints:

- Do not submit before the user reviews important input/output paths and the mathematical or statistical method, unless explicitly told to skip review.
- Do not download raw data or large intermediates without explicit approval.

The remote protocol is an approval gate, not an automatic permission to push or submit.

## Slurm Log And Live Progress Requirements

Every new Slurm workflow must satisfy all of these checks:

1. `.out` states the task content before computation, including analysis name, system/run, task or frame selection, resolved parameters, and output directory.
2. `.out` records start time, host, job/array identifiers, exact command or resolved parameters, end time, and final exit status.
3. `.err` carries unbuffered, promptly flushed `tqdm`-style frame progress, warnings, tracebacks, and diagnostics. Python workers use `python -u` or an equivalent unbuffered mode and send progress to stderr.
4. Array tasks use distinct `.out` and `.err` paths and record task ID, system/run, and output directory.
5. Aggregation tasks record dependency job IDs, input result root, and output summary/figure files.
6. Before a new large submission, run a smoke test and confirm that both `.out` and `.err` contain useful runtime information.
7. Keep server tests, temporary scripts, logs, and intermediate outputs under the recorded remote test-agent directory; never use shared `/tmp`.

Do not submit the large job when the smoke test does not prove both log channels are usable.

## Optional Literature Workflow

Use this only when the method depends on papers.

If references are missing, ask for 3-5 seed papers or suggest the type of papers needed. Do not fabricate references.

If the project uses a local literature library, keep source PDFs in `literature_library/pdfs/`. This folder is intentionally not tracked by Git. Extract reusable notes into `docs/literature/literature_knowledge_base.md` and method consequences into `docs/literature/method_implications.md`.

Default literature workflow:

1. Create or update `docs/literature/reference_manifest.csv`.
2. Read the provided references or source files.
3. Extract method-relevant information, not only general background.
4. Write `docs/literature/literature_review.md`.
5. Write `docs/literature/method_implications.md`.
6. Update `docs/definitions.md` if the literature confirms definitions, thresholds, windows, units, or assumptions.
7. Update `docs/method_registry.md` if the literature identifies methods to implement, avoid, or compare.

## Task Modes

Every task should be treated as one of:

- `design only`: clarify scientific question, definitions, inputs, outputs, and validation. Do not edit analysis code.
- `implement + verify`: make scoped edits and run lightweight checks.
- `interpret results`: read outputs and explain meaning. Do not edit code unless asked.

If the user does not specify a mode, infer the safest mode.

## Grill-Me / Clarification Mode

When the user asks to "grill me", "问清楚", "帮我弄清楚需要确定什么", or starts a new analysis without enough detail:

1. Do not implement immediately.
2. Draft a short analysis contract from what is known.
3. Ask only the missing high-risk questions.
4. Prefer one focused question at a time when the uncertainty is conceptual.
5. Use a checklist only after the main uncertainty is clear.

## Analysis Contract Rule

Before implementing any analysis:

1. Draft an analysis contract from the user's request.
2. If important fields are missing, ask only the missing high-risk questions.
3. Do not start implementation until the contract is clear enough.
4. Save or update the contract when it is useful for future work.

Required contract fields:

- module/workstream
- scientific question
- literature basis or reference set, when method design depends on papers
- local repo branch and allowed edit scope
- remote runtime path if server execution is needed
- sbatch script path and server run command, if server execution is needed
- input data paths
- systems and run range
- metric definition
- window/threshold definition
- expected output files
- validation checks
- files/folders that must not be touched

## Output Requirements

Every formal analysis should produce:

- documented command or script entry point
- trial tables/figures under `outputs/test/` during checking
- reviewed final tables/figures under `outputs/final/`
- a compact `outputs_manifest.json` based on `docs/codex/outputs_manifest.template.json`
- remote run command and log path, when applicable
- sbatch script and resource estimate, when applicable
- literature/method note when the analysis follows a specific paper or reference method
- short README or method note if the method is new or changed
- lightweight verification record

Keep the manifest small for local work: record the analysis id, status, command, outputs, and checks. Add Git, input, method, literature, or remote fields only when they materially help reproduction or retrieval.

## Project State Updates

After meaningful work:

1. Report changed files.
2. Report Git status and whether changes are committed, if relevant.
3. Report checks run and whether they passed.
4. State assumptions and unresolved decisions.
5. Update `PROJECT_INDEX.md` if Git/remote paths, canonical files, definitions, or next actions changed.
6. Update `docs/method_registry.md` if a method became canonical or legacy.
7. Update `docs/definitions.md` if a definition was confirmed or changed.
8. Update `docs/literature/` if new references changed method guidance.

## Editing Safety

If editing Chinese or other non-ASCII text on Windows:

- Prefer direct patches or UTF-8 files.
- Avoid piping source text through PowerShell into Python.
- After editing, check that text was not corrupted into repeated question marks.
