# Literature Review Prompt

Use this when a new project or method needs literature grounding.

```text
Mode: design only。

请先读：
1. PROJECT_INDEX.md
2. AGENTS.md
3. docs/definitions.md
4. docs/method_registry.md
5. docs/codex/literature_review_workflow.md

我希望先做参考文献阅读和方法综述，不要写分析代码。

参考文献来源：
<粘贴 DOI / arXiv / 标题 / PDF 路径 / BibTeX，或者说明需要你帮我先提出应找哪类文献>

请完成：
1. 建立或更新 docs/literature/reference_manifest.csv；
2. 逐篇阅读并提取和方法有关的信息；
3. 写 docs/literature/literature_review.md；
4. 写 docs/literature/method_implications.md；
5. 总结这些文献对 definitions.md 的影响；
6. 总结这些文献对 method_registry.md 的影响；
7. 给出后续第一个最小可执行分析建议。

要求：
- 不要编造没读过的文献内容；
- 区分“文献原文/结果”和“你的推断”；
- 如果需要联网查 DOI 或最新信息，先说明并使用可靠来源；
- 综述重点服务于后续分析方法选择，不要写成泛泛背景介绍。
```

