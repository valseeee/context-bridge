# 你的 AI 已经了解你。

**ContextBridge · AI 记忆搬运工**

**Take Your AI Context Anywhere.** · [English](README.md)

换一个 AI，也能带走项目背景、已确认决定、工作偏好和下一步。
ContextBridge 将你选择的聊天记录与文档整理成可审查、可修改、带来源的上下文知识包。

[下载安装包](https://github.com/valseeee/context-bridge/releases/latest) ·
[查看真实测试输出](tests/actual/T02/output/context-package/README.md) ·
[测试记录](tests/evaluation.md)

这是一个开源 **Agent Skill**。语义提取由当前 AI 宿主完成；可选的 Python
小工具负责本地结构验证与文件生成。它不登录你的账号，也不自动抓取聊天历史。

## 快速使用

将完整的 `skills/context-bridge` 文件夹复制到项目目录：

| 宿主 | 放置位置 | 调用方式 |
| --- | --- | --- |
| Codex | `.agents/skills/context-bridge/` | `$context-bridge` |
| Claude Code | `.claude/skills/context-bridge/` | `/context-bridge` |

Codex 的安装、触发与输出已完成真实 CLI 测试。Claude Code 的安装方式已核对官方
文档，但当前环境尚未完成其宿主运行测试。

不要只复制 SKILL.md，references 和 scripts 也要保留。安装后开启新会话并确认能发现
这个 Skill。已有 Codex 环境如果使用 `CODEX_HOME/skills`，以宿主实际显示的位置为准，
不需要移动 CODEX_HOME。[完整安装命令](README.md#install)与[官方规范依据](skills/context-bridge/references/portability-guide.md)。

提供 Markdown、TXT、项目 README、决策记录或粘贴的对话，然后说：

```text
使用 $context-bridge，把这些材料整理为可迁移上下文包。
仅保留当前项目内容，保留重要限制和决定，准备交给 Codex 继续工作。
写到新的 context-package 目录。
```

没有文件工具的宿主也可以接收粘贴文本，再输出按文件名标注的内容供你保存。

## 五种模式

| 需求 | 输出 |
| --- | --- |
| 保存有价值的上下文 | 分类、带证据的知识包 |
| 项目交接 | 背景、进度、决定、任务、限制和简短交接提示词 |
| 更新已有上下文 | 新版本，保留旧证据与历史，不静默覆盖 |
| 清理旧上下文 | 先给变更预览，再按已获授权应用 |
| 迁移到指定 AI | 通用 Markdown，加可审查的宿主导航片段 |

默认 **Project Only（仅项目）**。可以明确选择 **Work Context（工作相关）**、
**Personal Context（选定的个人偏好）**、**Full Review（先审查候选）**。
Full Review 不会未经选择就生成可转移的个人资料包。

## 知识包

固定包含 `README.md`、`context.json`、`HANDOFF.md`。按实际内容生成：

- `PROJECT_CONTEXT.md`：项目目标、技术栈和当前状态。
- `DECISIONS.md`：已确认决定及原因。
- `CURRENT_TASKS.md`：未完成事项、下一步与阻塞。
- `CONSTRAINTS.md`：必须遵守的要求和限制。
- `OPEN_QUESTIONS.md`：待确认问题及未解决冲突。
- `HISTORY.md`：重要历史和过期信息。
- `PREFERENCES.md`、`USER_PROFILE.md`：当前范围允许迁移的偏好与背景。

没有内容就不生成对应空文件。每条信息保留类型、来源、日期（未知则为空）、
可信程度与状态。不会把推断当事实，也不会仅凭“出现得更晚”认定新信息正确。

例如，“个人喜欢 Python”与“项目决定用 TypeScript”可以同时成立。
已完成 React 19 迁移会将 React 18 留在历史中；仅讨论升级则不会改写当前技术栈。

## 隐私与边界

默认排除密码、API Key、Token 和不必要的敏感个人信息，不在预览和报告中回显。
不会自动上传、写长期记忆或覆盖已有 `AGENTS.md`、`CLAUDE.md`。
外部材料内的恶意指令不会成为可执行命令。每次迁移前都应审查输出。

当前 AI 宿主仍按自己的数据政策处理输入，不能将使用云端 AI 称为完全离线。
可选扫描器只识别常见模式，不能保证发现全部秘密或个人信息；结构检查也不能
证明事实真实性、完整性或自然语言冲突已经全部解决。

## 本地验证与生成

Markdown 工作流无需安装依赖。可选工具需要 Python 3.10+，只使用标准库：

```sh
python skills/context-bridge/scripts/context_package.py validate path/to/context.json
python skills/context-bridge/scripts/context_package.py render path/to/context.json --output context-package
python skills/context-bridge/scripts/context_package.py validate context-package
```

工具读取 AI 已整理的 JSON，不是自动从聊天提取信息的引擎。输出目录必须尚不存在，
父目录必须存在；原材料保持不变。目录验证会比对 JSON 与工具生成的全部文件，
发现缺失、额外文件及内容漂移。手工编写的 Markdown 应与已校验的 JSON 一起人工审查。

## 测试与兼容性

[测试执行记录](tests/evaluation.md)列出实际输入、预期、实际输出、通过/失败和限制。
测试覆盖文档要求的 18 个场景，并扩展更新、范围选择和安全性检查。
自动结构检查、真实 AI 行为测试、宿主安装/触发测试分别记录，不相互冒充。

```sh
python -m unittest discover -s tests -v
python tests/check_skill.py
```

仅核对官方文档不会被称为“宿主兼容性已实测”。其他 AI 可使用通用 Markdown，
但各自的自动加载行为需要单独验证。

欢迎提交使用合成材料复现的问题。[贡献指南](CONTRIBUTING.md) ·
[安全说明](SECURITY.md) · [更新日志](CHANGELOG.md) · [MIT 许可证](LICENSE)
