# Maintenance Prompt

Use this weekly or at the end of a project stage.

```text
Mode: interpret results。

请检查 PROJECT_INDEX.md、AGENTS.md、docs/definitions.md、docs/method_registry.md，以及最近的 outputs_manifest.json。

不要改分析代码，除非我明确要求。

请总结：
1. 本地 Git 和远程运行容器关系是否清楚；
2. 当前已经稳定的方法；
3. 当前还没锁定的定义；
4. 当前文献综述是否足够支持方法选择；
5. 哪些文献结论应该写入 definitions.md 或 method_registry.md；
6. 哪些脚本/notebook 应该标为 canonical；
7. 哪些文件应该标为 legacy/debug；
8. 哪些结果已经 cite-ready；
9. 当前项目最大的 3 个风险；
10. 下一阶段最该推进的 3 件事。

如果需要更新项目文档，请先列出建议改动，再等我确认。
```
