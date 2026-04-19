# 🤖 AI Tools - 命令行 AI 工具箱

> 一个简洁高效的命令行 AI 工具集，支持翻译、总结、润色、问答等功能。基于各大免费 LLM API，无需额外配置，开箱即用。

## ✨ 功能

- 📝 **翻译** - 中英互译及其他多语言翻译
- 📖 **总结** - 文章/文本一键摘要
- ✍️ **润色** - 文本改写与优化
- 💬 **问答** - 智能问答助手
- 🎯 **标题生成** - 为文章/视频生成吸引人的标题
- 🔍 **关键词提取** - 从文本中提取核心关键词

## 🚀 快速开始

### 安装

```bash
pip install ai-tools
```

或者克隆使用：

```bash
git clone https://github.com/050612s/ai-tools.git
cd ai-tools
pip install -r requirements.txt
```

### 配置 API

工具支持多种免费 LLM API，配置环境变量即可：

```bash
# SiliconFlow (推荐，免费额度)
export SILICONFLOW_API_KEY="your-api-key"
export SILICONFLOW_BASE_URL="https://api.siliconflow.cn/v1"

# 或者使用 OpenAI 兼容接口
export OPENAI_API_KEY="your-api-key"
export OPENAI_BASE_URL="https://your-api-endpoint.com/v1"
```

### 使用

```bash
# 翻译
ai-tools translate "Hello world"

# 总结文章
echo "你的长文本内容..." | ai-tools summarize

# 润色
ai-tools polish "原始文本"

# 问答
ai-tools ask "什么是人工智能？"

# 生成标题
ai-tools title "文章内容摘要"

# 提取关键词
ai-tools keywords "文本内容"
```

### 交互模式

```bash
ai-tools chat  # 进入对话模式
```

## 🛠️ 项目结构

```
ai-tools/
├── main.py              # 主入口
├── translator.py         # 翻译模块
├── summarizer.py         # 总结模块
├── polisher.py           # 润色模块
├── qa.py                 # 问答模块
├── title_gen.py          # 标题生成
├── keywords.py           # 关键词提取
├── api_client.py         # LLM API 客户端
├── requirements.txt
└── README.md
```

## 📋 环境要求

- Python 3.8+
- requests
- 有网络连接

## 📄 License

MIT License
