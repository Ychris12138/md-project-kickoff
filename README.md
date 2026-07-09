# MD Project Kickoff

## 适用场景 / Use cases

这个 Codex skill 适合需要逐步澄清、跨线程延续并保持可复现性的科研或代码分析项目。它以本地 Git 为事实来源，用轻量项目地图和工作规则保存上下文，并可按需扩展文献综述、远程运行和 Slurm `sbatch` 工作流。

This Codex skill is for research and code-analysis projects that evolve through gradual clarification, span multiple threads, and need reproducible project state. It keeps local Git as the source of truth, stores context in a lightweight project map and working rules, and optionally expands into literature review, remote execution, and Slurm `sbatch` workflows.

- 新科研或代码分析项目 / New research or code-analysis projects
- 尚未完全确定定义、方法或数据路径的项目 / Projects with evolving definitions, methods, or data paths
- 需要多个 Codex 线程持续协作的项目 / Projects continued across multiple Codex threads
- 需要可选文献依据或远程批处理的项目 / Projects that may need literature grounding or remote batch execution

[中文](#中文) | [English](#english)

## 中文

### 核心能力

- 默认建立最小 Git-first 项目结构，不要求开局时填完所有信息。
- 生成 `README.md`、`PROJECT_INDEX.md`、`AGENTS.md`、定义中心、方法注册表和分析合约。
- 只追问 3-5 个高风险问题，并允许把未知项标记为 `unclear`。
- 每个正式分析使用轻量 `outputs_manifest.json` 记录产物和验证结果。
- 仅在需要时启用文献综述、远程 Git 和 `sbatch` 三阶段协议。
- 默认保护已有文件；使用 `--force` 时先备份到 `.project-kickoff-backup/<timestamp>/`。

### 安装

将 `<github-owner>` 替换为仓库所有者：

```powershell
gh repo clone <github-owner>/md-project-kickoff "$env:USERPROFILE\.codex\skills\md-project-kickoff"
```

macOS 或 Linux：

```bash
gh repo clone <github-owner>/md-project-kickoff ~/.codex/skills/md-project-kickoff
```

也可以用 `npx` 直接从 GitHub 运行初始化器：

```bash
npx github:<github-owner>/md-project-kickoff --target <project_root>
```

更新已有安装：

```powershell
git -C "$env:USERPROFILE\.codex\skills\md-project-kickoff" pull --ff-only
```

安装后开启新的 Codex 线程并调用 `$md-project-kickoff`。

### 使用

最小初始化：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

建立不加入 Git 的本地文献库，用于存放 PDF 并沉淀小知识库：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --with-literature-library
```

需要文献和远程运行结构时：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --profile full
```

默认 `.gitignore` 与学科无关。可选领域规则位于 `assets/md-project-kickoff-template/gitignore-profiles/`。

## English

### Core capabilities

- Creates a minimal Git-first scaffold without requiring every decision up front.
- Generates `README.md`, `PROJECT_INDEX.md`, `AGENTS.md`, definitions, a method registry, and an analysis contract.
- Asks only 3-5 high-risk questions and permits unknown values to remain `unclear`.
- Uses a compact `outputs_manifest.json` for every formal analysis.
- Adds literature review, remote Git, and the three-stage `sbatch` protocol only when needed.
- Preserves existing files by default; `--force` first backs them up under `.project-kickoff-backup/<timestamp>/`.

### Install

Replace `<github-owner>` with the repository owner:

```powershell
gh repo clone <github-owner>/md-project-kickoff "$env:USERPROFILE\.codex\skills\md-project-kickoff"
```

On macOS or Linux:

```bash
gh repo clone <github-owner>/md-project-kickoff ~/.codex/skills/md-project-kickoff
```

You can also run the initializer directly from GitHub with `npx`:

```bash
npx github:<github-owner>/md-project-kickoff --target <project_root>
```

Update an existing installation:

```powershell
git -C "$env:USERPROFILE\.codex\skills\md-project-kickoff" pull --ff-only
```

Open a new Codex thread after installation and invoke `$md-project-kickoff`.

### Usage

Minimal initialization:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

Create a non-Git local literature library for PDFs and a small knowledge-base starter:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --with-literature-library
```

Add literature and remote-run scaffolding:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --profile full
```

The default `.gitignore` is domain-neutral. Optional domain profiles live under `assets/md-project-kickoff-template/gitignore-profiles/`.
