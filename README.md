# 快题方案逻辑检查

面向文字概念、草图和完整快题成图的 Codex Skill，检查方案逻辑、纸面证据、实现硬伤与现实边界。

## 安装

```powershell
codex plugin marketplace add AlvaroViento/KT_Skill_Exoplanet --ref main && codex plugin add quick-sketch-logic-review@exoplanet-skills
```

安装后新建一个 Codex 任务，再使用 `$quick-sketch-logic-review`。

## 更新已有安装

```powershell
codex plugin marketplace upgrade exoplanet-skills && codex plugin remove quick-sketch-logic-review@exoplanet-skills && codex plugin add quick-sketch-logic-review@exoplanet-skills
```

## 仓库结构

```text
.agents/plugins/marketplace.json
plugins/quick-sketch-logic-review/
  .codex-plugin/plugin.json
  skills/quick-sketch-logic-review/
```
