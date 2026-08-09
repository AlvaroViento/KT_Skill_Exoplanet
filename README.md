# 快题方案逻辑检查

面向文字概念、草图和完整快题成图的 Skill，检查方案逻辑、纸面证据、实现硬伤与现实边界。支持 Codex 和 Claude Code。

## Codex 安装

```powershell
codex plugin marketplace add AlvaroViento/KT_Skill_Exoplanet --ref main && codex plugin add quick-sketch-logic-review@exoplanet-skills && Write-Host '安装完成。Codex 输入“使用 $quick-sketch-logic-review 审查…”；支持文字、草图/画板和完整成图，用于概念发展、草稿修改与成图复盘。'
```

安装后新建一个 Codex 任务，再使用 `$quick-sketch-logic-review`。

### Codex 更新已有安装

```powershell
codex plugin marketplace upgrade exoplanet-skills && codex plugin remove quick-sketch-logic-review@exoplanet-skills && codex plugin add quick-sketch-logic-review@exoplanet-skills && Write-Host '更新完成。Codex 输入“使用 $quick-sketch-logic-review 审查…”即可。'
```

## Claude Code 安装

在 Claude Code 中执行：

```text
/plugin marketplace add AlvaroViento/KT_Skill_Exoplanet
/plugin install quick-sketch-logic-review@exoplanet-skills
/reload-plugins
```

安装后可使用 `/quick-sketch-logic-review:quick-sketch-logic-review`，也可以直接描述任务让 Claude 自动调用。

## 仓库结构

```text
.agents/plugins/marketplace.json                 # Codex marketplace
.claude-plugin/marketplace.json                   # Claude Code marketplace
plugins/quick-sketch-logic-review/
  .codex-plugin/plugin.json                       # Codex manifest
  .claude-plugin/plugin.json                      # Claude Code manifest
  skills/quick-sketch-logic-review/               # 两个平台共用的唯一 Skill 源
```

平台 manifest 分开维护，`SKILL.md`、`references/`、`schemas/`、`scripts/` 和 `evals/` 不复制。Claude manifest 刻意不写固定 `version`，Git 安装会按提交版本更新；Codex 继续在自己的 manifest 中维护语义化版本。
