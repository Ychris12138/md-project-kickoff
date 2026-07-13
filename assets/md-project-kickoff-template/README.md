# Agent-Neutral MD Project Kickoff Template

这个模板包用于在新科研/分析项目的第一个 Agent 任务中建立“项目操作系统”。

它不要求你一开始就知道所有定义和方法。它的目标是让 Agent：

- 先建立 Git 和远程运行关系：本地是主仓库，远程是运行容器。
- 先追问关键问题，而不是直接写代码。
- 先收集、阅读和总结关键参考文献，把文献方法沉淀成后续分析依据。
- 把不确定定义记录下来。
- 建立项目地图、定义中心、方法注册表和分析合约机制。
- 后续每次任务都能从项目上下文继续，而不是重新扫描整个文件夹。

## 推荐使用方式

在新项目第一个 Agent 任务中复制 `prompts/first_thread_prompt.md`，把 `<project_path>`、`<project_name>` 和自然语言项目目标替换掉。

最小开局 prompt：

```text
这是一个新项目，路径是 <project_path>。
请使用 md-project-kickoff skill 中自带的模板和初始化脚本。
用 Git-first + grill-me / 追问澄清 的方式，先帮我建立项目启动结构。
不要直接写分析代码。

请完成：
1. 判断项目根目录应该在哪里；
2. 先检查/初始化本地 Git；
3. 规划本地主仓库和远程运行容器的连接；
4. 建立 PROJECT_INDEX.md 和 AGENTS.md；
5. 建立 docs/definitions.md、docs/method_registry.md、docs/literature/ 和 docs/codex/；
6. 建立参考文献阅读与综述流程；
7. 把还不确定的问题列成“需要我确认的问题”；
8. 给出第一批应阅读的参考文献类型和第一个最小可执行分析建议。
```

## 模板内容

| 文件 | 用途 |
|---|---|
| `PROJECT_INDEX.template.md` | 新项目项目地图模板 |
| `AGENTS.template.md` | 新项目共享 Agent 工作规则模板 |
| `docs/definitions.template.md` | 项目定义中心模板 |
| `docs/method_registry.template.md` | 方法注册表模板 |
| `docs/literature/reference_manifest.template.csv` | 参考文献清单模板 |
| `docs/codex/analysis_contract_template.md` | 分析任务合约模板（兼容路径） |
| `docs/codex/git_remote_workflow.md` | 本地 Git 主仓库 + 远程运行容器标准流程 |
| `docs/codex/literature_review_workflow.md` | 参考文献阅读、方法综述和项目沉淀流程 |
| `docs/codex/remote_sbatch_task_protocol.md` | 本地实现、远程 sbatch、结果取回三阶段协议 |
| `docs/codex/output_manifest_schema.md` | 结果产物 manifest 规范 |
| `docs/codex/migration_checklist.template.md` | 跨项目方法迁移清单 |
| `docs/codex/project_scaffold_checklist.md` | 新项目骨架检查清单 |
| `.gitignore.template` | 科研/分析项目 Git 忽略模板 |
| `prompts/*.md` | 常用第一任务、设计、实现、解释、维护 prompt |
| `examples/critical_first_thread_prompt.md` | critical 项目第一任务示例 |
| `adapters/claude/CLAUDE.template.md` | Claude Code 项目入口 |
| `adapters/cursor/project-kickoff.mdc` | Cursor 项目规则入口 |

`docs/codex/` 是历史兼容路径，内容本身不依赖 Codex；后续项目可迁移到更通用的 `docs/workflows/`。

## 五项优化对应关系

| 优化 | 新项目文件/机制 |
|---|---|
| Git-first 项目布局 | 本地 Git 主仓库 + 远程 bare repo + 远程 runtime checkout |
| 项目地图 | `PROJECT_INDEX.md` |
| 分析合约 | `docs/codex/analysis_contract_template.md` + `AGENTS.md` |
| 方法注册表 | `docs/method_registry.md` |
| 定义中心 | `docs/definitions.md` |
| 文献综述 | `docs/literature/` + `docs/codex/literature_review_workflow.md` |
| 产物说明 | 每个正式分析输出 `outputs_manifest.json` |

## 工作原则

1. 每个项目先有本地 Git；本地仓库是主仓库。
2. 远程服务器是运行容器，不是唯一真相来源。
3. 项目文件是活地图，不是一次性完美蓝图。
4. 参考文献综述要服务于方法选择，而不是只写成普通读书报告。
5. 可以大量写“未确定”，这样 Agent 会知道必须先问你。
6. 合约主要由 Agent 草拟，你只负责确认高风险定义。
7. 每个正式分析都要有可复现入口、产物说明和轻量验证。
8. 每周或每个阶段结束时，让 Agent 更新项目地图、定义文件、文献综述和方法注册表。
