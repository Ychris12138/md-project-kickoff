# Analysis Contract

Use this before `implement + verify` work.

The user does not need to fill every field manually. The Agent should draft this from the request, then ask only the missing high-risk questions.

## 1. Task Header

```yaml
mode: <design only | implement + verify | interpret results>
project_root: <project path>
module: <module/workstream>
analysis_id: <short stable id>
date: <YYYY-MM-DD>
local_branch: <branch>
commit_scope: <files/folders the Agent may edit>
do_not_touch: <raw data, unrelated modules, old outputs>
```

## 2. Scientific Question

```text
I want to know whether/how <quantity> changes with <condition/system/window>.
```

## 3. Literature Basis

Fill this section if the method, metric, threshold, or interpretation depends on papers.

```yaml
reference_manifest: docs/literature/reference_manifest.csv
literature_review: docs/literature/literature_review.md
method_implications: docs/literature/method_implications.md
key_references:
  - <paper id / DOI / title>
literature_status: <not needed | seed needed | reading | summarized>
```

## 4. Inputs

```yaml
systems:
  - label: <system label>
    input_root: <path>
    run_range: <run range>
    required_files:
      - <relative file path>
missing_run_policy: <skip and record | fail fast | ask user>
large_file_policy: <reference only | copy allowed?>
```

## 5. Git / Remote Runtime

Fill this section if server execution is needed.

```yaml
local_repo_is_source_of_truth: true
remote_ssh_alias: <alias>
remote_bare_repo: <path or not needed for this task>
remote_runtime_checkout: <path>
remote_test_agent_dir: <path>
remote_data_root: <path>
remote_results_root: <path>
local_test_output_dir: outputs/test/<analysis_id>
local_final_output_dir: outputs/final/<analysis_id>
sync_policy: <what is pushed, pulled, and copied back>
remote_run_command: <command or unclear>
remote_log_path: <path or unclear>
sbatch_script: <path or not needed>
sbatch_submit_command: <command or unclear>
expected_runtime: <estimate or unclear>
```

## 6. Definitions To Lock

| Definition | Value | Source/status |
|---|---|---|
| metric | `<definition>` | confirmed/unclear |
| window | `<definition>` | confirmed/unclear |
| threshold | `<value>` | confirmed/unclear |
| coordinate/PBC convention | `<definition>` | confirmed/unclear |
| statistics | `<method>` | confirmed/unclear |
| units | `<units>` | confirmed/unclear |

## 7. Expected Outputs

| Output | Purpose | Required? |
|---|---|---|
| `<csv/json>` | `<purpose>` | yes/no |
| `<figure>` | `<purpose>` | yes/no |
| `outputs_manifest.json` | output inventory | yes |

Suggested output root:

```text
results/<system>/<analysis_id>/
```

If running remotely, also specify:

```text
<remote_results_root>/<analysis_id>/
```

Selected results should eventually be downloaded to:

```text
<local_project_root>/outputs/final/<analysis_id>/
```

## 8. Verification

```yaml
local_checks:
  - <command>
smoke_test:
  required_before_large_submission: true
  command: <small representative command>
  out_log_check: <task/system/run/parameters/start/end/status>
  err_log_check: <unbuffered live frame progress/warnings/diagnostics>
review_before_commit:
  required: true
  review_focus:
    - input paths
    - raw trajectory/topology paths
    - output paths
    - sbatch command
    - mathematical/statistical method
server_checks:
  - <command>
success_signal:
  - <expected file/count/plot/log>
```

## 9. Questions For User

Only unresolved high-risk questions:

- `<question>`

## 10. Final Thread Deliverable

The Agent should return:

- changed files
- local Git status and commit recommendation
- remote commands used or recommended
- review package for input/output paths and method summary before commit/push
- sbatch job id and estimated finish time, after submission
- result files downloaded to outputs, after user reports completion
- checks run
- pass/fail status
- assumptions
- unresolved decisions
- next action
- whether `PROJECT_INDEX.md`, `docs/definitions.md`, or `docs/method_registry.md` should be updated
- whether `docs/literature/` should be updated
