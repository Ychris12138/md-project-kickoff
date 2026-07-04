# Implement + Verify Prompt

```text
Mode: implement + verify。

请先读 PROJECT_INDEX.md、AGENTS.md、docs/definitions.md、docs/method_registry.md 和本次 analysis contract。
如果任务真的需要服务器运行，再补读对应的 remote/sbatch 协议。

请根据合约实现。

要求：
1. 只改 contract 允许的文件；
2. 本地 Git 是 source of truth，先检查当前分支和工作区状态；
3. 如需服务器运行，使用 PROJECT_INDEX.md 里的 SSH alias 和 remote runtime checkout；
4. 不移动、不删除、不覆盖原始数据；
5. 不扫描大型结果/轨迹/缓存目录，除非合约需要；
6. 写好对应 sbatch 脚本；
7. 输出必须包含 outputs_manifest.json；
8. 跑轻量本地检查；
9. 先给我审阅包：输入位置、输出位置、sbatch 命令、关键数学方法、预计运行时间；
10. 我审阅通过后再 commit/push；
11. push 后 ssh 到服务器确认代码已更新到最新版，再运行 sbatch；
12. 提交后报告 job id、日志位置、输出位置和预计完成时间；
13. 如果任务未跑完，可以结束并等待我通知；
14. 我通知跑完后，再 ssh 检查结果，挑选关键轻量结果下载到 outputs 文件夹并分析；
15. 完成后说明是否需要更新 PROJECT_INDEX.md、definitions.md、method_registry.md。

Analysis contract:
<paste contract here>
```
