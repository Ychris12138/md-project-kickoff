# Project Kickoff Skill

用于快速初始化 Codex 驱动的科研与代码分析项目。

## 主要能力

- 建立 Git-first 项目结构：本地仓库是 source of truth，远程服务器是 runtime container。
- 生成 `PROJECT_INDEX.md`、`AGENTS.md`、定义中心、方法注册表和分析合约。
- 建立参考文献阅读、方法综述和方法沉淀流程。
- 规范本地实现、用户审阅、commit/push、远程 `sbatch`、结果取回和分析的三阶段流程。
- 使用 `outputs_manifest.json` 管理远程结果、同步范围和 cite-ready 产物。

## 安装

将本仓库放入 Codex 的个人 skills 目录：

```text
~/.codex/skills/project-kickoff
```

Windows 示例：

```text
C:\Users\<username>\.codex\skills\project-kickoff
```

重新打开一个 Codex 线程后即可调用。

## 使用

在新项目第一条线程中输入：

```text
使用 $project-kickoff 初始化这个新项目。
本地项目路径是 <project_root>。
请先建立 Git、PROJECT_INDEX、AGENTS、definitions、method registry、literature 和远程 sbatch 工作流，不要直接写分析代码。
```

也可以直接运行初始化脚本：

```bash
python <skill_dir>/scripts/init_project_kickoff.py --target <project_root>
```

脚本默认不会覆盖已有项目文件；需要覆盖时使用 `--force`，仅查看计划时使用 `--dry-run`。

## 隐私与安全

- 仓库不包含真实服务器地址、用户名、密钥、令牌或个人数据路径。
- 模板中的 `<remote_alias>`、`<remote_home>`、`<project_root>` 等都需要在项目本地填写。
- 不要把 SSH 私钥、访问令牌、原始轨迹或大型结果提交到 Git。
- 远程运行路径和原始数据位置应记录在项目自己的 `PROJECT_INDEX.md` 或本地配置中。

## 结构

```text
project-kickoff/
  SKILL.md
  README.md
  agents/openai.yaml
  scripts/init_project_kickoff.py
  assets/project-kickoff-template/
```

