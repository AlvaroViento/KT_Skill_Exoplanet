---
name: quick-sketch-logic-review
description: Concisely review time-limited design sketch proposals across interaction, industrial, product, service, spatial, architectural, landscape, and planning disciplines. Use this when asked to review, diagnose, revise, or reflect on written ideas, sketches, design boards, or complete design-exercise presentations. Focus on identifying logical gaps between the problem, target users or objects, strategy, implementation, and outcomes, as well as critical factual errors and feasibility issues. Recommend only a small number of minimal, high-impact revisions.

---
# 快题方案逻辑检查

把快题视为有限时间内的设计论证。只挑影响结论的重点，不把审查扩展成完整产品咨询。

## 加载参考

- 始终读取 [review-rules.md](references/review-rules.md)。
- 遇到会改变结论的现实、技术、法规、标准或理论主张时，读取 [evidence-policy.md](references/evidence-policy.md) 并核验。

## 选择模式

- `idea_review`：文字 Idea、提纲、零散草图或未完成画板。检查方案本身是否成立。
- `final_review`：完成度较高、已有明确版式和阅读路径的整张快题。检查方案逻辑与图面说服力。

用户指定模式时服从用户。无法确定时默认 `idea_review`，继续执行，不为模式选择中断用户。

## 复述方案

先用一句话复述现有方案：谁或什么对象，在什么情境下面临什么问题，方案通过什么方式产生什么改变。

只整理用户明确提供或图中可辨认的信息。不要替作者补齐缺失原因、功能、角色或结果；必要推断必须标明“推测”。

## 审查流程

### Idea 检查

1. 复述方案。
2. 检查问题、对象与情境、策略、实现、结果五项及其连接。
3. 找出最可能击穿方案的逻辑断点或实现硬伤。
4. 只在必要时核验会改变判断的关键事实。
5. 默认给出一至两个问题；只有第三个问题同样会改变方案结论时才保留。每个问题只给一个最小修改。

不要在此模式下以“图面没有证明”为由批评尚未完成的方案。可以指出待验证假设，但不要把它写成成图缺口。

### 成图复盘

1. 只提取图面可见、可读的内容；看不清时写“无法辨认”，不要写“没有”。
2. 按五项通用模型检查方案逻辑与实现硬伤。
3. 必要时核验关键事实。
4. 严格区分“现实中成立”和“图面已经证明”：外部资料只能支持前者，不能替代图面证据。
5. 按重画价值排序，默认给出一至两个问题；只有第三个问题同样值得优先重画时才保留。

## 输出

使用以下最短结构：

```markdown
## 方案复述
一句话。

## 最重要的问题
1. **问题**：一句话。
   - 依据：一句话。
   - 最小修改：一个动作。

## 需要确认
- 仅列确实影响判断的不可读信息、待验证事实或不确定项。
```

没有“需要确认”时省略该节。该节最多两项，只列答案会改变判断的阻塞项，不要把已经诊断的问题改写成问题再问一遍。

保持短句。每个问题的“问题、依据、最小修改”各限一句；除引用链接外，默认把整份审查控制在 400 个汉字以内。一个问题足以击穿方案时不要凑数。

## 限制

- 不给总分，不用长篇教学代替判断。
- 不使用“加强调研”“丰富体验”“完善方案”等空话。
- 不预设方案必须是 App、硬件、服务、空间或系统。
- 不因缺少精确预算、完整商业模式、技术架构或全部异常流程而单独判定失败。
- 不扩写新的设计方案，除非用户明确要求。
