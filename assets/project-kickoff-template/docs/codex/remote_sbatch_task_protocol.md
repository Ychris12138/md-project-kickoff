# Remote Sbatch Task Protocol

This protocol is required for tasks that implement analysis locally and run it on a remote server with `sbatch`.

Core model:

```text
local repo = edit, test, review, commit, push
remote runtime checkout = pull latest code, run sbatch, inspect logs/results
thread outputs folder = selected lightweight results for user-facing delivery
```

## Stage 1. Local Implementation And Review Package

Work locally first.

Required steps:

1. Read `PROJECT_INDEX.md`, `AGENTS.md`, `docs/definitions.md`, `docs/method_registry.md`, and the relevant analysis contract.
2. Confirm local Git branch and working tree state.
3. Implement code changes in the local repository.
4. Add or update the corresponding `sbatch` script.
5. Run lightweight local correctness checks:
   - unit tests if available
   - script `--help`
   - parser/config checks
   - small fixture/dry-run
   - shell syntax check for `sbatch` scripts when appropriate
6. Prepare a review package for the user before commit/push.

The review package must include:

| Item | Required content |
|---|---|
| Code changes | files changed and purpose |
| Inputs | exact input directories/files |
| Raw data | raw trajectory/topology paths and read-only policy |
| Outputs | exact output root, tables, figures, logs, manifest |
| Sbatch | script path and submit command |
| Resources | partition, nodes/tasks/cpus/memory/time if known |
| Runtime estimate | best estimate and uncertainty |
| Math/method | key formulas, thresholds, windows, statistics |
| Checks | local checks run and pass/fail |
| Risks | assumptions, missing definitions, likely failure modes |

Do not commit/push until the user approves the review package, unless explicitly told to proceed without review.

After approval:

```bash
git status --short --branch
git add <changed files>
git commit -m "<message>"
git push <runtime_remote> <branch>
```

## Stage 2. Remote Update And Sbatch Submission

After pushing local commits:

1. SSH to the server:

```bash
ssh <remote_alias>
```

2. Enter runtime checkout:

```bash
cd <remote_runtime_checkout>
```

3. Update and verify code:

```bash
git fetch
git status --short --branch
git pull --ff-only
git rev-parse --short HEAD
```

4. Submit job:

```bash
sbatch <script> <args>
```

5. Report:

- remote host/alias
- runtime checkout path
- commit hash
- sbatch command
- job id
- log path
- output path
- requested resources
- estimated completion time

If the job will keep running, stop after reporting submission status and wait for the user to notify completion.

## Stage 3. Completion, Retrieval, And Interpretation

When the user reports the job is complete:

1. SSH to remote.
2. Check job/log status:

```bash
cd <remote_runtime_checkout>
tail -n 80 <log file>
```

3. Inspect outputs.
4. Prefer `outputs_manifest.json` for selecting files.
5. Download only key lightweight results to the local thread/project `outputs` folder.
6. Analyze results.
7. Report:

- files downloaded
- main results
- sanity checks
- caveats
- whether outputs match expected paths/definitions
- next-step recommendations

Never download raw trajectories, full simulation data, or large intermediate outputs unless explicitly approved.

## Required Sbatch Script Checklist

Each `sbatch` script should make these clear:

- project/runtime working directory
- environment activation
- input paths
- raw trajectory/topology paths
- output root
- log path
- analysis id
- command being run
- resource request
- failure behavior

## Result Download Destination

Default local destination:

```text
<current Codex thread workspace>/outputs/<analysis_id>/
```

If the user gives a project-specific output path, use that instead.

