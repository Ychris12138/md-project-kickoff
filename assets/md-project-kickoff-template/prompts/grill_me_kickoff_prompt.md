# Grill-Me Kickoff Prompt

Use this when the project is still blurry and you want Codex to ask clarifying questions before structure or code.

```text
Mode: design only。

请用 grill-me / 追问澄清 的方式帮我梳理这个项目。
不要写代码，不要建立复杂工作流。

请先根据我目前的描述，整理：
1. 你已经确定的内容；
2. 你认为高风险但不确定的内容；
3. 为了建立 Git/远程运行关系、PROJECT_INDEX.md、definitions.md、method_registry.md，必须问我的问题；
4. 最少 3 个、最多 7 个关键问题。

请优先问会影响后续分析定义的问题，比如：
- 本地项目根目录在哪里；
- 是否已经有 Git；
- 远程 SSH alias 和运行路径是什么；
- 科学问题到底是什么；
- 数据在哪里；
- 哪些文件不能动；
- 系统/run 如何命名；
- 关键指标/阈值/窗口如何定义；
- 第一个最小分析应该是什么。
```
