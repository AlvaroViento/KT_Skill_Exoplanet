# 审查模型

## 目录

1. 输入与可见证据
2. 方案模型
3. Finding
4. 状态与排序

## 1. 输入与可见证据

`ReviewInput`：

- `input_mode`: `text_concept | board_draft | final_sheet`
- `review_goal`: `develop | revise | retrospective | benchmark`
- `raw_text`: 原始文字或 `null`
- `images`: 图像引用列表
- `user_constraints`: 用户明确约束
- `locale`: 默认 `zh-CN`

`VisibleEvidence`：

- `id`: 稳定、可引用的标识
- `source_type`: `text | image_text | diagram | interface | illustration | layout`
- `content`: 实际可见内容，不写修复后的推断
- `location`: 段落、区域或版面位置；无法定位时为 `null`
- `visibility`: `explicit | inferred | unreadable | absent`
- `confidence`: `0..1`
- `supports`: 被支持的主张 ID

提取时遵守：

1. 先复述，后评价。
2. 每个视觉项标注可见状态。
3. 图像质量不足时降低置信度，不声称缺失。
4. `absent` 只用于已经检查且确实没有发现的区域。

## 2. 方案模型

统一逻辑链：

`问题 → 对象 → 设计策略 → 实现 → 效果`

### 问题

- `subject`: 谁受到影响
- `context`: 在什么具体情境
- `obstacle`: 被什么障碍或冲突阻断
- `consequence`: 造成什么损失、风险或负担
- `current_workaround`: 当前如何应对
- `gap`: 现有方式为什么不足

推荐句式：某类人在某个具体情境中，因为某种障碍或冲突，持续产生某种损失，而现有方式存在明确缺口，设计有介入空间。

### 对象

- `identity`: 人群身份
- `recurring_context`: 反复出现的情境
- `current_behavior`: 当前行为
- `constraints`: 特殊约束或能力边界
- `conflict`: 两种目标之间的冲突
- `distinction`: 与相邻人群的区别

执行替换测试：若换成相邻人群后问题和策略几乎不变，则对象没有参与推导。

### 策略

- `premise`: 可核验前提
- `evidence_type`: `industry_consensus | human_assumption | theory | mixed | unknown`
- `intervention`: 设计干预
- `mechanism`: 被改变的中间机制
- `proximal_change`: 先发生的近端变化
- `boundary`: 适用边界

推荐句式：因为【前提】，所以采用【干预】，通过改变【中间机制】，促使对象产生【近端变化】，进而回应【目标问题】。

### 实现

- `actors`: 使用者、服务者、付出者、受益者及责任
- `core_flow`: 核心步骤
- `technical_principle`: 足以解释可行性的轻量原理
- `inputs`: 可获得输入
- `processing`: 处理或判断
- `outputs`: 输出
- `claimed_effect`: 所声称效果

只要求足以排除明显硬伤的信息，不要求完整架构。

## 3. Finding

每条 Finding 包含：

- `module`: `problem | target_user | strategy | implementation | cross_link | presentation`
- `category`: `fact_error | logic_break | paper_gap | hard_bug | unreadable | strength`
- `severity`: `fatal | major | minor`
- `status`: `pass | weak | broken | insufficient_information`
- `confidence`: `high | medium | low`
- `evidence_refs`: 当前材料中的证据 ID
- `external_source_refs`: 外部事实来源 ID
- `explanation`: 判断及影响
- `minimal_fix`: 一个首选最小动作
- `suggested_visual_form`: 一句话、小流程、对比图、角色关系图、输入处理输出图或 `null`

任何 `fatal` 或 `major` 必须含具体 `minimal_fix`。外部来源 ID 不得混入 `evidence_refs`。

## 4. 状态与排序

状态：

- `pass`: 信息明确、连接成立、事实无明显冲突。
- `weak`: 方向成立，但证据、机制或表达不足。
- `broken`: 明确事实错误、逻辑冲突或硬伤。
- `insufficient_information`: 输入无法支持可靠判断。

严重度：

- `fatal`: 方案基础失效，后续优点无法抵消。
- `major`: 明显削弱说服力或造成关键断点。
- `minor`: 影响局部清晰度、完整度或可信度。

置信度：

- `high`: 输入明确，且有直接纸面证据或多个可靠来源。
- `medium`: 部分依赖合理推断或单一来源。
- `low`: 图像不可读、语义歧义或外部证据不足。

排序：`fatal` → 跨模块/硬伤 `major` → 纸面缺口 `major` → `minor`。基础性、跨模块影响、修复杠杆越高越靠前；不确定性越高越靠后。
