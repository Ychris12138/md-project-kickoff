# First Thread Prompt

Copy this into the first Codex thread for a new project.

```text
这是一个新项目：

Project name: <project_name>
Project path: <project_path>

请使用 `$md-project-kickoff` skill。

请用 Git-first + grill-me / 追问澄清 的方式先做轻量初始化。
不要直接写分析代码。

请完成：
1. 判断项目根目录应该在哪里；
2. 检查或初始化本地 Git，并把本地仓库作为 source of truth；
3. 建立最小项目文档：PROJECT_INDEX.md、AGENTS.md、docs/definitions.md、docs/method_registry.md、docs/codex/analysis_contract_template.md；
4. 询问是否需要建立不加入 Git 的本地文献库 `literature_library/`，用于随时放入 PDF 并沉淀到 `docs/literature/literature_knowledge_base.md`；
5. 只在项目确实需要时，再补远程运行、文献综述或 sbatch 说明；
6. 列出还需要我确认的 3-5 个高风险问题；
7. 给出第一个最小可执行分析建议。

项目背景：
<用自然语言写几句话即可，不需要完整。>

如果远程信息暂时不完整，不要自己猜；只在确实要远程运行时再补。
如果参考文献暂时没有给出，先不要展开文献综述，除非方法明显依赖论文。
如果我选择建立文献库，请使用 `--with-literature-library` 初始化或补齐结构，并说明 PDF 不会加入 Git。
```
