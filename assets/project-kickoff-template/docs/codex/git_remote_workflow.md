# Git And Remote Runtime Workflow

This project uses a Git-first workflow.

Principle:

```text
local repository = source of truth
remote server path = runtime container
```

## 1. Recommended Topology

Use three roles:

```text
Local working repo
  -> where Codex edits, commits, and maintains project docs/code

Remote bare repo
  -> push target on the server, e.g. <remote_home>/git/<project>.git

Remote runtime checkout
  -> non-bare working directory used to run jobs, e.g. <remote_home>/<project>/code
```

Why not push directly into the runtime checkout?

- A checked-out branch in a non-bare repo can reject pushes.
- The runtime checkout may contain logs, temporary files, and generated outputs.
- Separating the bare repo from the runtime checkout makes the workflow safer and easier to recover.

## 2. Information To Record In PROJECT_INDEX.md

| Item | Example |
|---|---|
| Local project root | `<local_project_root>` |
| Local branch | `main` |
| Remote SSH alias | `server` |
| Remote bare repo | `<remote_home>/git/<project>.git` |
| Remote runtime checkout | `<remote_home>/<project>/code` |
| Remote data root | `<remote_data_root>` |
| Remote results root | `<remote_results_root>` |

## 3. First-Time Local Setup

From the local project root:

```bash
git init
git branch -M main
```

Create or verify `.gitignore` before the first commit. It should usually exclude:

```gitignore
__pycache__/
.pytest_cache/
.venv/
venv/
env/
tmp/
logs/
results/
*.log
*.dcd
*.xtc
*.trr
*.tpr
*.gro
*.pdb
*.nc
*.h5
```

Then commit the project scaffold:

```bash
git add PROJECT_INDEX.md AGENTS.md README.md docs configs scripts src tests notebooks
git commit -m "Initialize project scaffold"
```

Adjust the `git add` paths to match the actual project.

## 4. First-Time Remote Setup

On the remote server:

```bash
mkdir -p <remote_home>/git
git init --bare <remote_home>/git/<project>.git
mkdir -p <remote_home>/<project>
git clone <remote_home>/git/<project>.git <remote_home>/<project>/code
```

On local:

```bash
git remote add runtime ssh://<remote_alias>/<absolute_remote_repo_path>
git push -u runtime main
```

On remote, update the runtime checkout:

```bash
ssh <remote_alias> "cd <remote_home>/<project>/code && git pull --ff-only origin main"
```

## 5. Normal Update Flow

Local:

```bash
git status --short --branch
git add <changed files>
git commit -m "<short message>"
git push runtime main
```

Remote:

```bash
ssh <remote_alias> "cd <remote_runtime_checkout> && git pull --ff-only origin main"
```

Then run:

```bash
ssh <remote_alias> "cd <remote_runtime_checkout> && <run command>"
```

## 6. Inspecting Remote State

Use the SSH alias and runtime path recorded in `PROJECT_INDEX.md`:

```bash
ssh <remote_alias>
cd <remote_runtime_checkout>
git status --short --branch
ls
```

For logs:

```bash
ssh <remote_alias> "cd <remote_runtime_checkout> && find logs -maxdepth 2 -type f | tail"
```

## 7. Results And Sync Policy

Large raw outputs should normally stay remote.

Formal analysis outputs should include:

```text
outputs_manifest.json
```

Use the manifest to decide which files to fetch:

- `sync: true`: lightweight tables, figures, manifests, logs, summaries.
- `sync: false`: large intermediate outputs or files that can be regenerated.

Preferred local destination:

```text
review/<analysis_id>/
```

or:

```text
results_synced/<analysis_id>/
```

## 8. Safety Rules

- Do not run `rm -rf` on local or remote project paths unless explicitly approved.
- Do not use `rsync --delete` unless explicitly approved.
- Do not commit large raw trajectories or generated result directories.
- Do not push directly into the remote runtime checkout unless the workflow was deliberately configured that way.
- If local and remote branches diverge, stop and ask before merging/rebasing.
