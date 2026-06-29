# AGENTS.md

This file defines how Codex should work inside this project.

## Project Operating Rules

1. Read `PROJECT_INDEX.md` before doing project work.
2. Treat the local Git repository as the source of truth unless the user says otherwise.
3. Treat the remote server path as a runtime container/check-out used for running jobs, inspecting logs, and producing outputs.
4. Read the Git/remote section of `PROJECT_INDEX.md` before suggesting push, pull, SSH, sync, or server-run commands.
5. Read `docs/definitions.md` before changing scientific definitions, thresholds, windows, labels, units, or coordinate conventions.
6. Read `docs/method_registry.md` before creating, replacing, or declaring an analysis method canonical.
7. Read `docs/literature/` before using literature-supported methods, definitions, thresholds, or claims.
8. Read `docs/codex/remote_sbatch_task_protocol.md` before implementing or running any server-side sbatch task.
9. Do not inspect large raw data, trajectory, result, cache, or temporary folders unless the task requires it.
10. Do not move, delete, overwrite, or download raw data unless explicitly approved.
11. Prefer existing project conventions over inventing new layouts.
12. If a definition is unclear, ask the user instead of guessing.

## Git And Remote Runtime Rules

Before code implementation in a new project:

1. Ensure the local project is a Git repository.
2. Ensure `.gitignore` excludes large raw data, generated results, logs, caches, virtual environments, and temporary folders.
3. Make an initial local commit containing only project structure and lightweight documentation.
4. Record remote SSH alias, remote bare repo path, remote runtime checkout path, remote data root, and remote results root in `PROJECT_INDEX.md`.
5. Prefer this topology:

```text
local repo -> remote bare repo -> remote runtime checkout
```

Do not push directly into a checked-out non-bare remote working tree unless the user has explicitly configured and approved that workflow.

Standard remote run flow:

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

## Remote Sbatch Task Protocol

For server-side analysis tasks, use a three-stage workflow.

### Stage 1: Local implementation and review package

Do locally:

1. Modify code in the local repository.
2. Check correctness with lightweight local tests, lint/help commands, dry-runs, or small fixtures when available.
3. Write or update the corresponding `sbatch` script.
4. Verify the `sbatch` script references input paths, raw trajectory paths, output paths, logs, environments, and working directories from project files such as `PROJECT_INDEX.md`, `docs/definitions.md`, configs, or analysis contracts.
5. Prepare a review summary for the user before commit/push.

The review summary must highlight:

- input files and directories
- raw trajectory/topology locations
- output directory and generated files
- log location
- sbatch command
- expected runtime estimate and resource request
- key mathematical/statistical steps of the analysis
- sanity checks or validation signals

Do not commit/push until the user has reviewed the important input/output locations and mathematical method summary, unless the user explicitly asked to skip review.

After review approval:

1. Commit locally.
2. Push to the configured remote bare repo.

### Stage 2: Remote update and sbatch submission

After push:

1. SSH to the server using the alias in `PROJECT_INDEX.md`.
2. Enter the remote runtime checkout.
3. Confirm the remote code is updated to the pushed commit or branch tip.
4. Run the approved `sbatch` command.
5. Report job id, command, log path, output path, resource request, and estimated finish time.

If the job is still running and no further useful work can be done, stop and wait for the user to notify Codex when the job is complete.

### Stage 3: Result retrieval and interpretation

When the user says the job is complete:

1. SSH to the server.
2. Check job/log status and output files.
3. Use `outputs_manifest.json` if available to decide which files are important.
4. Download only key lightweight results to the current thread/project `outputs` folder, unless the user asks for a different destination.
5. Analyze the results.
6. Summarize findings, caveats, and next-step recommendations.

Do not download raw trajectories or large intermediate files unless explicitly approved.

## Literature Review Rules

For new scientific projects or new analysis methods, Codex should ask whether a small reference set exists before finalizing method design.

The user may provide:

- paper titles
- DOI links
- arXiv links
- PDFs
- BibTeX/RIS entries
- prior notes

If references are incomplete, Codex may ask for 3-8 seed papers or suggest the type of papers needed. Do not fabricate references.

Default literature workflow:

1. Create or update `docs/literature/reference_manifest.csv`.
2. Read the provided references or source files.
3. Extract method-relevant information, not only general background.
4. Write `docs/literature/literature_review.md`.
5. Write `docs/literature/method_implications.md`.
6. Update `docs/definitions.md` if the literature confirms definitions, thresholds, windows, units, or assumptions.
7. Update `docs/method_registry.md` if the literature identifies methods to implement, avoid, or compare.

The literature review should include:

- problem framing
- per-paper summary
- method extraction table
- definitions/thresholds used in each paper
- data/simulation setup if relevant
- validation/sanity checks used in each paper
- limitations and risks
- implications for this project
- recommended first analysis methods

If the user asks for latest papers or live DOI/source verification, use current web/source lookup and cite links. If the user only provides local PDFs or files, rely on those files and state the source scope.

## Task Modes

Every task should be treated as one of:

- `design only`: clarify scientific question, definitions, inputs, outputs, and validation. Do not edit analysis code.
- `implement + verify`: make scoped edits and run lightweight checks.
- `interpret results`: read outputs and explain meaning. Do not edit code unless asked.

If the user does not specify a mode, infer the safest mode:

- unclear scientific definition -> `design only`
- clear contract and implementation requested -> `implement + verify`
- existing tables/figures/logs provided -> `interpret results`

## Grill-Me / Clarification Mode

When the user asks to “grill me”, “问清楚”, “帮我弄清楚需要确定什么”, or starts a new analysis without enough detail:

1. Do not implement immediately.
2. Draft a short analysis contract from what is known.
3. Ask only the missing high-risk questions.
4. Prefer one focused question at a time when the uncertainty is conceptual.
5. Use a checklist only after the main uncertainty is clear.

High-risk questions usually involve:

- scientific quantity
- input data path
- run range or systems
- threshold/window definition
- coordinate/PBC convention
- expected outputs
- validation or sanity checks
- files/folders that must not be touched

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

The user does not need to write the full contract manually. Codex should help draft it.

## Output Requirements

Every formal analysis should produce:

- documented command or script entry point
- tables/figures under a clear output directory
- `outputs_manifest.json`
- remote run command and log path, when applicable
- sbatch script and resource estimate, when applicable
- literature/method note when the analysis follows a specific paper or reference method
- short README or method note if the method is new or changed
- lightweight verification record

`outputs_manifest.json` should list:

- file path
- file type
- purpose
- system/run/window
- parameter set or analysis id
- whether to sync/download
- whether suitable for citation/downstream use
- remote path and local destination, when applicable

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
