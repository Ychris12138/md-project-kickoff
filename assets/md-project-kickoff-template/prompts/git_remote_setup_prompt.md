# Git + Remote Runtime Setup Prompt

Use this when the project exists locally but Git/remote runtime are not set up yet.

```text
Mode: design only, then implement only after confirming the plan.

请使用 `md-project-kickoff` skill，并读取项目内的 `docs/codex/git_remote_workflow.md`。

目标：
把这个项目整理成 Git-first 工作流：
本地仓库作为 source of truth，远程服务器作为 runtime container。

请先检查并汇报：
1. 本地项目根目录；
2. 当前是否已经是 Git repo；
3. 当前分支和工作区状态；
4. .gitignore 是否足够排除大数据、结果、日志、缓存；
5. 需要我确认的远程信息：
   - SSH alias；
   - remote bare repo path；
   - remote runtime checkout path；
   - remote data root；
   - remote results root。

在我确认前，不要执行远程创建、push、pull 或删除操作。

确认后请建立或更新：
1. PROJECT_INDEX.md 的 Git And Remote Runtime section；
2. AGENTS.md 的 Git/remote rules；
3. docs/codex/git_remote_workflow.md；
4. 初始本地 commit，如果项目还没有 commit。
```
