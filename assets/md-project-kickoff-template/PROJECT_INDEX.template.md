# Project Index

Last updated: `<YYYY-MM-DD>`

Root: `<project_root>`

Local repo role: source of truth

Remote role: runtime container

## 0. Codex Start Here

When opening a new Codex thread for this project:

1. Read this file first.
2. Read `AGENTS.md`.
3. Check the Git/remote section before changing code or suggesting server commands.
4. Read `docs/definitions.md` and `docs/method_registry.md` only when the task touches methods or scientific definitions.
5. If implementation is needed, draft or update an analysis contract first.

Default rules:

- Do not scan large raw data, trajectory, cache, result, or temporary folders unless the task asks for them.
- Do not move, delete, overwrite, or download raw data without explicit approval.
- Treat local Git as the canonical project state unless the user says otherwise.
- Treat the remote path as a runtime checkout/container used for running jobs and inspecting logs.
- Use `outputs/test/` for trial outputs and `outputs/final/` for reviewed deliverables unless a task-specific contract says otherwise.
- If a definition is missing or unclear, ask the user instead of inventing it.
- Prefer small design steps before implementation.
- Update this file when canonical files, active workstreams, or next actions change.

## 1. Git And Remote Runtime

Use this section only if the project needs Git or remote execution.

Recommended model:

```text
local working repo  ->  remote bare repo  ->  remote runtime checkout
source of truth         push target           server-side run directory
```

| Item | Value | Status |
|---|---|---|
| Local project root | `<local_project_root>` | confirmed/unclear |
| Local branch | `<main or project branch>` | confirmed/unclear |
| Remote SSH alias | `<ssh alias>` | confirmed/unclear |
| Remote runtime checkout | `<remote_runtime_checkout>` | confirmed/unclear |
| Remote data root | `<remote data root>` | confirmed/unclear |
| Remote results root | `<remote results root>` | confirmed/unclear |

Standard sync flow:

```text
local commit -> git push runtime <branch> -> ssh remote "cd <runtime> && git pull --ff-only" -> run jobs remotely -> fetch/summarize lightweight outputs
```

Remote inspection:

```bash
ssh <remote_ssh_alias>
cd <remote_runtime_checkout>
git status --short --branch
```

## 2. Project Goal

Short description:

```text
<What is this project trying to understand?>
```

Main scientific questions:

- `<question 1>`
- `<question 2>`

## 3. Current Data

| Dataset/system | Path | Location | Status | Notes |
|---|---|---|---|---|
| `<label>` | `<path>` | local/server/unknown | available/partial/unknown | `<notes>` |

Raw data policy:

- `<policy 1>`
- `<policy 2>`

## 4. Current Workstreams

| Workstream | Status | Canonical files | Next action |
|---|---|---|---|
| `<analysis>` | idea/design/active/canonical/blocked | `<files>` | `<next step>` |

Status meanings:

- `idea`: only a question or direction exists.
- `design`: definitions, inputs, outputs, and validation are being clarified.
- `active`: implementation or trial runs are underway.
- `canonical`: current recommended method or result line.
- `blocked`: needs user decision, missing data, or external run.

## 5. Key Files To Read First

| File | Role |
|---|---|
| `PROJECT_INDEX.md` | Project map and current state |
| `AGENTS.md` | Codex operating rules |
| `docs/definitions.md` | Definitions, labels, thresholds, windows, units |
| `docs/method_registry.md` | Current best implementation of each method |
| `docs/codex/analysis_contract_template.md` | Contract template for new analysis work |
| `docs/codex/output_manifest_schema.md` | Result manifest schema |
| `docs/codex/outputs_manifest.template.json` | Small manifest starter for each formal analysis |

Optional full-profile files:

- `docs/codex/git_remote_workflow.md`
- `docs/codex/remote_sbatch_task_protocol.md`
- `docs/codex/literature_review_workflow.md`

## 6. Definitions To Confirm

These are intentionally allowed to be incomplete.

- `<definition or threshold not yet decided>`
- `<coordinate/window/unit convention not yet decided>`

## 7. Literature And Method References

Use this section only if the project is literature-driven.

| Topic | Key references | Method implications | Status |
|---|---|---|---|
| `<topic>` | `<paper ids or DOIs>` | `<definitions, metrics, checks to reuse>` | needed/reading/summarized |

Default literature outputs, when needed:

- `docs/literature/reference_manifest.csv`
- `docs/literature/literature_review.md`
- `docs/literature/method_implications.md`
- optional local PDF library: `literature_library/pdfs/` (not tracked by Git)
- optional searchable notes: `docs/literature/literature_knowledge_base.md`
- optional: `docs/literature/references.bib`

## 8. Files And Folders To Avoid By Default

| Path/pattern | Reason |
|---|---|
| `<raw_data_path>` | raw data, do not move/delete/copy |
| `literature_library/` | local PDF/source library, not tracked by Git |
| `outputs/test/` | trial generated outputs |
| `outputs/final/` | final generated deliverables |
| `results/` | may contain large or generated outputs |
| `tmp/` | temporary outputs |
| `.venv/`, `__pycache__/`, `.pytest_cache/` | tool/cache folders |

## 9. Standard New-Thread Prompt

```text
This is <project_name>.
First read PROJECT_INDEX.md and AGENTS.md.
Mode: <design only | implement + verify | interpret results>
Goal: <one concrete goal>

Treat the local repo as the source of truth and the remote path as the runtime container.
If remote information is needed, use the SSH alias/path recorded in PROJECT_INDEX.md.
If the analysis contract is incomplete, draft it from my request and ask only the missing high-risk questions.
Do not scan large raw data/result/cache folders unless needed.
```

## 10. Maintenance Checklist

Update this file when:

- A new workstream starts.
- Git/remote paths or branch conventions change.
- A reference review adds or changes method guidance.
- A method becomes canonical or legacy.
- A definition changes.
- A new result line becomes suitable for downstream use.
- The next action changes.
