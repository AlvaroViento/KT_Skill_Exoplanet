# 外星人设计studio｜快题方案逻辑检查

把文字概念、草图或完整快题成图交给 AI，快速找出方案逻辑断点、纸面证据不足、实现硬伤和现实约束，并获得可以直接落到图面上的最小修改建议。

支持 Codex 和 Claude Code。

## 它能帮你做什么

- **概念发展**：把零散想法还原成“问题—对象—策略—实现—效果”的逻辑链。
- **草稿修改**：区分已表达、未表达和不可读内容，指出应该补什么图、删什么内容。
- **成图复盘**：检查阅卷路径、模块衔接、技术可信度和最需要重画的位置。
- **对标学习**：从优秀方案中提取可复用的结构、图示和表达方法。
- **现实核验**：遇到法规、技术、理论或行业主张时，联网核验会影响结论的关键事实。

## 可以提交什么

- 一段方案描述、题目或设计提纲
- 草图、白板、便签或过程截图
- 产品、交互、服务、空间、建筑、景观或规划类完整快题成图

图片模糊或文字不可辨认时，Skill 会明确标记不确定项，不会把猜测当成图面证据。

## 安装到 Codex

在 PowerShell 中运行：

```powershell
codex plugin marketplace add AlvaroViento/KT_Skill_Exoplanet --ref main
codex plugin add quick-sketch-logic-review@exoplanet-skills
```

安装后新建一个 Codex 任务，上传材料并输入：

```text
使用 $quick-sketch-logic-review 完整复盘这张快题成图。
```

## 安装到 Claude Code

在 Claude Code 中运行：

```text
/plugin marketplace add AlvaroViento/KT_Skill_Exoplanet
/plugin install quick-sketch-logic-review@exoplanet-skills
/reload-plugins
```

随后可以输入：

```text
/quick-sketch-logic-review:quick-sketch-logic-review 完整复盘这张快题成图。
```

也可以直接描述任务，由 Claude 自动判断是否调用该 Skill。

## 推荐提问方式

```text
使用这个 Skill 检查我的概念逻辑，并告诉我下一步最应该画哪三张图。

审查这张草稿，区分已呈现、未呈现和不可读的内容，给出最小补图方案。

完整复盘这张成图，优先指出最可能影响评审理解的三个问题。

对标这份优秀快题，提取我可以复用的版式、流程图和论证结构。
```

## 你会得到什么

- 对方案逻辑的准确还原和总体判断
- 按影响排序的最高优先级问题
- 每个问题的可见依据、判断和最小修复
- 可直接画成一句话、流程图、关系图或输入—处理—输出图的建议
- 必要的外部事实核验及适用限制
- 面向下一轮修改的执行顺序

它不会用一个总分代替诊断，也不会要求你把限时快题扩展成完整商业或工程方案。

## 更新

Codex：

```powershell
codex plugin marketplace upgrade exoplanet-skills
codex plugin remove quick-sketch-logic-review@exoplanet-skills
codex plugin add quick-sketch-logic-review@exoplanet-skills
```

Claude Code：

```powershell
claude plugin marketplace update exoplanet-skills
claude plugin update quick-sketch-logic-review@exoplanet-skills
```
