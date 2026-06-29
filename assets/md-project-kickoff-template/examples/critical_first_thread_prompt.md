# Critical Project First Thread Example

```text
这是一个研究项目，项目路径是：
<local_project_root>

请使用 `$md-project-kickoff` skill。

Mode: design only。

请先判断哪个目录应该作为项目根目录。
然后按 Git-first 方式建立项目启动结构：

1. 检查或初始化本地 Git，把本地作为 source of truth；
2. 规划远程运行容器：SSH alias、remote bare repo、remote runtime checkout、remote data root、remote results root；
3. PROJECT_INDEX.md；
4. AGENTS.md；
5. docs/definitions.md；
6. docs/method_registry.md；
7. docs/literature/reference_manifest.csv；
8. docs/literature/literature_review.md 或占位文件；
9. docs/literature/method_implications.md 或占位文件；
10. docs/codex/analysis_contract_template.md；
11. docs/codex/git_remote_workflow.md；
12. docs/codex/literature_review_workflow.md；
13. docs/codex/remote_sbatch_task_protocol.md；
14. docs/codex/output_manifest_schema.md；
15. docs/codex/migration_checklist.md。

不要实现分析代码。

这个项目大方向是研究水模型的结晶和 LLPT 之间的关系。
请用 grill-me / 追问澄清 的方式帮我梳理：

1. 核心科学问题；
2. 已有数据和 run 的路径；
3. 需要从 surface 项目迁移或参考的方法；
4. 必须先确认的定义，例如相标签、order parameter、结晶事件、时间窗口、阈值、单位；
5. 我应该提供哪些 LLPT/结晶关系的种子参考文献；
6. 本地和远程仓库/运行路径应该如何连接；
7. 第一个最小可执行分析应该是什么；
8. 哪些文件夹不能扫描、移动、删除或下载。

最后请列出“需要我确认的问题”，不要超过 7 个。
```
