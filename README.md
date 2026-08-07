# 快题方案逻辑检查

一个面向设计快题训练的 AI Skill。它不替你继续堆功能，而是检查问题、对象、策略、实现和结果能否连成一条成立的逻辑链。

适用于交互设计、工业设计、产品设计、服务设计及空间类设计等方向。

## 名称

| 用途 | 名称 |
|---|---|
| 对外名称 | 快题方案逻辑检查 |
| Skill 命令 | `$quick-sketch-logic-review` |
| 安装目录 | `quick-sketch-logic-review` |

`quick sketch` 对应“快题”，`logic review` 对应“逻辑检查”。中文名称增加“方案”，用于说明它检查的是方案逻辑，而不是绘画技法。

## 它能做什么

- 检查文字 Idea、初步草图和完整快题成图。
- 找出少数关键逻辑断点、事实错误和实现硬伤。
- 给出快题深度内可以执行的最小修改。
- 成图复盘时，区分“现实中成立”和“图面已经证明”。

它不提供总分，不默认补全完整商业模式、技术架构或全套产品方案。

## 安装

在 Codex CLI 中运行：

```bash
codex plugin marketplace add AlvaroViento/KT_Skill_Exoplanet && codex plugin add quick-sketch-logic-review@exoplanet-skills
```

安装后新开一个 Codex 会话即可使用。若只需要 Skill 文件，也可以把 [`plugins/quick-sketch-logic-review/skills/quick-sketch-logic-review`](plugins/quick-sketch-logic-review/skills/quick-sketch-logic-review) 复制到所用工具的 Skill 目录。

## 快速开始

```text
使用 $quick-sketch-logic-review 检查这个 Idea：
为社区独居老人设计邻里互助服务，老人发布需求，附近志愿者接单获得社区积分。
```

```text
使用 $quick-sketch-logic-review 复盘这张完整快题图，只告诉我最值得重画的两个地方。
```

完整用法见 [GUIDE.md](GUIDE.md)，发布清单见 [release-kit/CHECKLISTS.md](release-kit/CHECKLISTS.md)。

## License

[MIT](LICENSE)
