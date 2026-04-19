# 🤖 AI Tools - 命令行 AI 瑞士军刀

> 一套命令行工具，搞定翻译、总结、润色、问答、代码审查、批量处理。

**pip 安装后随时调用，无需打开网页。**

`ash
pip install ai-tools
ai-tools translate "Hello world"
ai-tools summarize -f article.txt
ai-tools polish "帮我润色这段话"
ai-tools batch -f list.txt -o translate -out result.txt
ai-tools qa -c "背景..." -q "问题..."
ai-tools review -f code.py
`

## 环境变量

`ash
export AI_API_KEY="your-siliconflow-key"   # 默认使用硅基流动
export AI_BASE_URL="https://api.siliconflow.cn/v1"
export AI_MODEL="Qwen/Qwen2.5-7B-Instruct"
`

## 支持模型

- 硅基流动（推荐，免费额度）
- OpenAI GPT-4 / GPT-3.5
- Anthropic Claude 3
- Google Gemini
- 本地 Ollama

## 命令一览

| 命令 | 说明 | 示例 |
|------|------|------|
| 	ranslate | 翻译 | i-tools translate "hello" -to 中文 |
| summarize | 总结 | i-tools summarize -f file.txt -s 简短 |
| polish | 润色 | i-tools polish "帮我润色..." |
| qa | 问答 | i-tools qa -c "背景" -q "问题" |
| eview | 代码审查 | i-tools review -f code.py |
| atch | 批量处理 | i-tools batch -f list.txt -o translate |