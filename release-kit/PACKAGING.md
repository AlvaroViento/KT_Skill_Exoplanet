# 发布打包规则

## 对外名称

- 产品名：`快题方案逻辑检查`
- Skill 名：`quick-sketch-logic-review`
- 调用命令：`$quick-sketch-logic-review`
- 版本格式：语义化版本，例如 `v1.0.0`

## 发布文件

### 1. Plugin 安装包

文件名：

```text
quick-sketch-logic-review-plugin-v1.0.0.zip
```

压缩包顶层包含：

```text
quick-sketch-logic-review/
├─ .codex-plugin/
└─ skills/
```

### 2. 新手使用包

文件名：

```text
快题方案逻辑检查-使用包-v1.0.0.zip
```

内容固定为：

```text
01-安装说明.pdf
02-使用指南.pdf
03-使用清单.pdf
03-使用清单-手机长图.png
04-示例.md
quick-sketch-logic-review-plugin-v1.0.0.zip
```

## 单一来源

- `README.md`：GitHub 首页与快速安装。
- `GUIDE.md`：完整使用说明，作为 PDF 指南源稿。
- `release-kit/CHECKLISTS.md`：清单 PDF 与长图的唯一源稿。
- `plugins/quick-sketch-logic-review/`：Plugin 安装包的唯一来源。

每次发布只修改源稿，再统一导出；不要直接修改 PDF、PNG 或压缩包内文件。
