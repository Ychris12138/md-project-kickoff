# First Thread Prompt

Copy this into the first Codex thread for a new project.

```text
这是一个新项目：

Project name: <project_name>
Project path: <project_path>

请使用 `$md-project-kickoff` skill。

请用 Git-first + grill-me / 追问澄清 的方式初始化项目。
不要直接写分析代码。

请完成：
1. 判断项目根目录应该在哪里；
2. 检查或初始化本地 Git，并把本地仓库作为 source of truth；
3. 规划远程运行容器：SSH alias、remote bare repo、remote runtime checkout、remote data root、remote results root；
4. 建立最小项目文档：PROJECT_INDEX.md、AGENTS.md、docs/definitions.md、docs/method_registry.md、docs/codex/；
5. 建立 docs/literature/，并准备参考文献阅读与方法综述流程；
6. 建立 Git/远程运行说明、远程 sbatch 任务协议和产物 manifest 规范；
7. 列出还需要我确认的问题，不超过 7 个；
8. 给出第一批应阅读的参考文献类型和第一个最小可执行分析建议。

项目背景：
<用自然语言写几句话即可，不需要完整。>

如果远程信息暂时不完整，请先把未知项写入 PROJECT_INDEX.md 的 Git/Remote section，不要自己猜。
如果参考文献暂时没有给出，请先在 docs/literature/reference_manifest.csv 中保留模板，并列出希望我提供的 3-8 篇种子文献类型。
```
