# recog-and-report: Word 模板报告自动化生成工具 & AI 技能

`recog-and-report` 是一个基于 `python-docx` 封装的 Word 模板报告与论文自动填充、生成工具。它既可以作为一个独立的 Python 命令行工具使用，也可以作为 **Antigravity AI 编码助手** 的自定义技能（Skill）进行部署，让 AI 助手能够高鲁棒性、高保真度地根据指定的 Word 模板生成格式严密的学术论文或技术报告。

---

## 🌟 核心特性

1. **模版结构自适应（Landmark Auto-Detection）**：无需硬编码段落索引。脚本自动识别模板中日期所在位置以标记封面终点，并自动定位分节符（Section Break）节点，确保“封面无页码，正文从第1页开始”的复杂排版完美保留。
2. **中英文字体混排（Mixed-Font Rendering）**：解决 `python-docx` 直接赋值导致英文/数字变为非预期字体的痛点。底层强制写入 XML 格式：中文采用宋体/黑体/楷体，英文和数字统一采用 Times New Roman，完美符合学术排版规范。
3. **自适应行间距与缩进**：全自动应用模板规定的“行间距固定值 20 磅”、“正文段落首行缩进 2 字符”以及各级标题的特定字号和粗细要求。
4. **全自动目录生成**：在分节符之前自动生成格式规范的目录，自动计算引点线（`……`）和页码对齐。
5. **模型无关的鲁棒性**：通过本地 Python 编译器，将复杂的格式修改代码从大模型的日常输出中抽离。大模型只需生成简单的结构化 `content.json`，运行脚本即可 100% 生成合格的 Word。

---

## 🚀 快速起步

### 1. 安装依赖
本项目依赖 `python-docx` 库，请确保本地已安装：
```bash
pip install python-docx
```

### 2. 准备数据文件 `content.json`
编写您的报告结构与正文数据，格式如下：
```json
{
  "title": "AI驱动创新与新质生产力发展的案例分析——以上汽通用五菱为例",
  "fields": {
    "学号": "2200300101",
    "姓名": "张三",
    "专业": "通信工程"
  },
  "toc": [
    {"text": "引言", "page": 1, "level": 0},
    {"text": "1  上汽通用五菱企业背景与数字化转型挑战", "page": 1, "level": 0},
    {"text": "  1.1  上汽通用五菱在汽车行业的定位与核心优势", "page": 1, "level": 1},
    {"text": "参考文献", "page": 11, "level": 0}
  ],
  "body": [
    {"type": "h1", "text": "引言"},
    {"type": "p", "text": "这里是引言的内容段落..."},
    {"type": "h1", "text": "1  上汽通用五菱企业背景与数字化转型挑战"},
    {"type": "h2", "text": "1.1  上汽通用五菱在汽车行业的定位与核心优势"},
    {"type": "p", "text": "正文段落二..."},
    {"type": "pb"},
    {"type": "ref_title", "text": "参考文献"},
    {"type": "ref_item", "text": "[1]  肖海棠. 上汽通用五菱智能制造发展战略研究[J]. 汽车与配件, 2021, (12): 45-49."}
  ]
}
```

### 3. 运行编译命令
使用终端命令一键生成排版合格的报告：
```bash
python3 scripts/auto_generator.py \
  --template "您的模板文件.docx" \
  --content "content.json" \
  --output "生成的论文.docx"
```

---

## 🤖 部署为 Antigravity 自定义技能

如果您使用的是 Antigravity 编码助手，可以将本项目作为技能引入，实现跨会话和跨项目的一键复用。

### 1. 全局部署 (推荐)
将本项目克隆或复制到您的全局配置目录下的 `skills` 文件夹中：
```bash
/Users/<YourUsername>/.gemini/config/skills/recog-and-report/
```
Antigravity 将自动发现并加载该技能，后续只需在对话中对 AI 指示：*“请根据 recog-and-report 技能，帮我撰写关于 X 主题的报告，模板为 Y.docx”*。

### 2. 项目局部部署
在您的项目根目录下创建 `.agents/skills.json` 文件并进行关联：
```json
{
  "entries": [
    { "path": "path/to/recog-and-report" }
  ]
}
```

---

## 🛠️ API 开发接口

如果您需要编写自定义生成脚本，可以直接调用 `scripts/docx_helper.py` 中的底层函数：
* `set_run_font(run, font_name, font_size_pt, bold, italic)`：设置混合字体属性。
* `set_cell_text(cell, text, font_name, font_size_pt, bold, align)`：安全修改单元格文本并保持居中/边框。
* `add_toc_entry(p_ref, text, page_num, indent_level)`：向前插入目录段落。
* `clean_doc_keep_sections(doc, cover_end_idx, section_break_idx)`：安全清空模板并保留节属性。
