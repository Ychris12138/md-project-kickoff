# MD Project Kickoff

Current release / 当前版本: **v1.0.2**

[Release v1.0.2](https://github.com/Ychris12138/md-project-kickoff/releases/tag/v1.0.2)

## 适用场景 / Use cases

这个 Agent Skill 适合需要逐步澄清、跨任务延续并保持可复现性的科研或代码分析项目。它以本地 Git 为事实来源，用轻量项目地图和共享工作规则保存上下文，并可按需扩展文献综述、远程运行和 Slurm `sbatch` 工作流。

This Agent Skill is for research and code-analysis projects that evolve through gradual clarification, span multiple agent tasks, and need reproducible project state. It keeps local Git as the source of truth, stores context in a lightweight project map and shared working rules, and optionally expands into literature review, remote execution, and Slurm `sbatch` workflows.

- 新科研或代码分析项目 / New research or code-analysis projects
- 定义、方法或数据路径仍在逐步确定的项目 / Projects with evolving definitions, methods, or data paths
- 需要跨多个 Agent 任务持续协作的项目 / Projects continued across multiple agent tasks
- 需要文献依据或远程批处理的项目 / Projects that need literature grounding or remote batch execution

[中文](#中文) | [English](#english)

## 中文

### 一键安装（推荐）

Windows PowerShell 5.1+：

```powershell
irm https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.ps1 | iex
```

macOS、Linux、WSL 或 Git Bash：

```bash
curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash
```

安装器需要 Node.js 18+，会自动检测并安装到当前机器上存在的标准技能目录：

| Agent | 默认目录 |
|---|---|
| Codex | `~/.codex/skills/md-project-kickoff/` |
| Claude Code | `~/.claude/skills/md-project-kickoff/` |
| Cursor | `~/.cursor/skills/md-project-kickoff/` |
| Agent Skills 通用目录 | `~/.agents/skills/md-project-kickoff/` |

安装完成后，在 Codex 中调用 `$md-project-kickoff`，在 Claude Code 或 Cursor 中调用 `/md-project-kickoff`。

### 安装器选项

默认只写入检测到的 Agent。需要显式创建所有支持目录时：

```bash
curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash -s -- --all
```

其他选项：

```bash
node bin/install.js --only codex,claude,cursor --dry-run
node bin/install.js --uninstall --only cursor
```

安装器可以重复运行，用于更新已安装版本；它只维护 `md-project-kickoff` 自己的技能目录。

### 初始化项目

安装后，最小初始化：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

同时建立 Claude Code 和 Cursor 的项目级入口：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --agent all
```

建立不加入 Git 的本地 PDF 文献库：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --with-literature-library
```

需要文献和远程运行结构时：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --profile full
```

### 备用方式

直接从 GitHub 运行初始化器：

```bash
npx -y github:Ychris12138/md-project-kickoff --target <project_root>
```

开发或离线场景可以手动 clone 到对应 Agent 的技能目录。默认 `.gitignore` 与学科无关；分子动力学等领域规则位于 `assets/md-project-kickoff-template/gitignore-profiles/`。

### 核心工作边界

- 本地 checkout 是唯一的开发、测试、编辑、commit 和 push 路径。
- SSH 服务器只负责接收代码、运行任务和保存大规模结果。
- Slurm 大任务提交前必须先做 smoke test，并确认 `.out/.err` 都有有效运行信息。
- `.out` 记录任务、system/run、参数、输出目录、开始/结束时间和退出状态。
- `.err` 使用无缓冲、实时刷新的 `tqdm` 帧进度。
- 试验结果放在 `outputs/test/`，审阅后的正式产物放在 `outputs/final/`。

## English

### One-command install (recommended)

Windows PowerShell 5.1+:

```powershell
irm https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.ps1 | iex
```

macOS, Linux, WSL, or Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash
```

The installer requires Node.js 18+ and detects the standard skill directories that exist on the machine:

| Agent | Default directory |
|---|---|
| Codex | `~/.codex/skills/md-project-kickoff/` |
| Claude Code | `~/.claude/skills/md-project-kickoff/` |
| Cursor | `~/.cursor/skills/md-project-kickoff/` |
| Agent Skills standard | `~/.agents/skills/md-project-kickoff/` |

After installation, invoke `$md-project-kickoff` in Codex, or `/md-project-kickoff` in Claude Code and Cursor.

### Installer options

The default installs only for detected Agents. To explicitly create every supported target:

```bash
curl -fsSL https://raw.githubusercontent.com/Ychris12138/md-project-kickoff/main/install.sh | bash -s -- --all
```

Other options:

```bash
node bin/install.js --only codex,claude,cursor --dry-run
node bin/install.js --uninstall --only cursor
```

The installer is safe to rerun for updates and only manages the `md-project-kickoff` skill directories.

### Initialize a project

Minimal initialization:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

Generate project-level Claude Code and Cursor entry points:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --agent all
```

Create a non-Git local PDF literature library:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --with-literature-library
```

Add literature and remote-run scaffolding:

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root> --profile full
```

### Alternative installation

Run the initializer directly from GitHub:

```bash
npx -y github:Ychris12138/md-project-kickoff --target <project_root>
```

For development or offline use, clone the repository into the relevant Agent skill directory. The default `.gitignore` is domain-neutral; optional domain profiles live under `assets/md-project-kickoff-template/gitignore-profiles/`.

### Core workflow boundaries

- The local checkout is the only development, testing, editing, commit, and push path.
- The SSH server receives reviewed code, runs jobs, and stores large results.
- Run a smoke test before large Slurm submissions and verify useful `.out` and `.err` logs.
- `.out` records the task, system/run, parameters, output directory, start/end times, and exit status.
- `.err` carries unbuffered, promptly flushed `tqdm`-style frame progress.
- Trial outputs go under `outputs/test/`; reviewed deliverables go under `outputs/final/`.
