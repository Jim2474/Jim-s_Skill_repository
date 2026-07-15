# Jim's Skill Repository

Claude Code 自建技能集合，包含 MCP 服务器、数学建模、论文写作、实验报告生成等工具。

## 技能清单

### MCP Servers

| 技能 | 说明 | 用法 |
|------|------|------|
| **vision-recognize** | 图片识别（非 OCR），返回结构化 Markdown | MCP 自动调用，提供图片路径即可 |

### 数学建模 & 科研

| 技能 | 说明 |
|------|------|
| **mm-modeling-copilot** | 端到端数学建模助手（NeurIPS 2025 MM-Agent 流程），支持问题分析 → 建模 → 求解 → 报告 |
| **paper-spine** | 论文写作工作流编排器（12 个子技能覆盖：选题、引用、重写、LaTeX、翻译、降 AI 率等） |

### 实验报告 & 文档

| 技能 | 说明 |
|------|------|
| **matlab-lab-report** | MATLAB 控制系统实验自动生成 A4 Word 报告 |
| **recog-and-report** | 识别指定 Word 模板的排版与格式要求，并在保留分节符、封面表格样式的前提下，自动填充/生成结构完整的学术论文或技术报告 |
| **tailored-resume-generator** | 根据 JD 自动生成针对性简历 |
| **design-md** | 将品牌设计系统应用到项目（支持 71 个品牌） |

### 学习笔记

| 技能 | 说明 |
|------|------|
| **learned/textbook-pdf-extraction** | 从中文教材 PDF 提取数学题目和答案 |

## 环境要求

- Windows 10/11
- Python 3.10+（venv 位于 `~/.claude/venv`）
- MATLAB（matlab-lab-report 技能需要）

## 安装

```bash
# 克隆仓库
git clone https://github.com/Jim2474/Jim-s_Skill_repository.git

# 安装 Python 依赖
pip install -r requirements.txt

# 注册 vision-recognize MCP 服务器（全局生效）
claude mcp add vision-recognize -s user -- ~/.claude/venv/Scripts/python <path>/vision-recognize/mcp_server.py
```

## 目录结构

```
.
├── vision-recognize/          # 图片识别 MCP 服务器
│   ├── mcp_server.py          # MCP 服务端（主入口）
│   ├── vision_recognize.py    # CLI 脚本（备用）
│   └── SKILL.md
├── mm-modeling-copilot/       # 数学建模助手
├── paper-spine*/              # 论文写作工作流（12 个子技能）
├── matlab-lab-report/         # MATLAB 实验报告生成
├── recog-and-report/          # Word 模板论文/报告自适应生成器
├── tailored-resume-generator/ # 简历生成器
├── design-md/                 # 品牌设计系统
├── learned/                   # 学习到的模式
├── examples/                  # 示例项目
└── requirements.txt           # Python 依赖
```

## 原 EXP Report Creator 文档

MATLAB 实验报告生成的详细用法见下方。

### 已验证流程

以 `examples/exp2` 为例：

1. 运行 MATLAB 实验脚本，生成文本输出和曲线图。
2. 将命令行输出按题号拆分。
3. 渲染成类似 MATLAB 命令窗口的白底输出图。
4. 将输出图和 MATLAB 曲线图排版进 A4 竖版 `.docx` 报告。

### 快速运行实验二示例

```powershell
matlab -batch "run('examples/exp2/experiment2_run.m')"
python examples/exp2/build_exp2_report.py
```

### 设计原则

- 报告必须是 A4 竖版，方便直接打印。
- 结果必须来自 MATLAB 真实运行，不手写伪造输出。
- 命令窗口结果默认使用 MATLAB 风格渲染图。
