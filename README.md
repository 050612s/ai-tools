# 🤖 AI Tools 工具箱

> 开源 AI 命令行工具箱，支持批量处理、代码审查、智能问答等。**零门槛，免费用。**

[![Stars](https://img.shields.io/github/stars/050612s/ai-tools?style=flat-square)](https://github.com/050612s/ai-tools)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/050612s/ai-tools/blob/main/LICENSE)

## ✨ 功能

| 命令 | 说明 |
|------|------|
| python main.py batch | 批量处理文件（翻译/摘要/改写） |
| python main.py review | 代码审查，找出 Bug 和优化点 |
| python main.py improve | 优化代码质量 |
| python main.py qa | 对代码/文档进行智能问答 |
| python main.py translate | 文档翻译 |
| python main.py summarize | 长文本摘要 |

## 🚀 快速开始

`ash
# 克隆项目
git clone https://github.com/050612s/ai-tools.git
cd ai-tools

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py --help
`

## 📦 使用示例

### 批量处理
`ash
python main.py batch --dir ./docs --task summarize
`

### 代码审查
`ash
python main.py review --file main.py
`

### 智能问答
`ash
python main.py qa --question "这个函数的时间复杂度是多少？" --file algorithm.py
`

## 💡 使用场景

- 📄 论文翻译与摘要
- 🔍 代码质量检查
- 📊 批量文档处理
- 💬 技术文档问答
- ✍️ 内容改写与润色

## 🛠️ 技术栈

- Python 3
- OpenAI API / SiliconFlow API
- 自然语言处理

## 📦 依赖

`
openai>=1.0.0
python-dotenv>=1.0.0
`

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

---

⭐ 如果对你有帮助，请给个 Star！你的支持是我维护的动力。