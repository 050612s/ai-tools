#!/usr/bin/env python3
"""
AI Tools - 命令行 AI 瑞士军刀
支持: 硅基流动 / OpenAI / Claude / Gemini / 本地 Ollama
pip install -U ai-tools
"""
import sys
import os
import json
import argparse
from typing import Optional

try:
    import requests
except ImportError:
    print("需要安装: pip install requests")
    sys.exit(1)


class AITools:
    def __init__(self, api_key: str = None, base_url: str = None, model: str = "Qwen/Qwen2.5-7B-Instruct"):
        self.api_key = api_key or os.environ.get("AI_API_KEY") or os.environ.get("SILICONFLOW_KEY")
        self.base_url = base_url or os.environ.get("AI_BASE_URL") or "https://api.siliconflow.cn/v1"
        self.model = model or "Qwen/Qwen2.5-7B-Instruct"

    def chat(self, prompt: str, system: str = None, json_mode: bool = False) -> str:
        """发送对话请求"""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4096,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}

        resp = requests.post(
            f"{self.base_url}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            json=payload, timeout=60
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]


def cmd_translate(text: str, from_lang: str = "auto", to_lang: str = "中文"):
    """翻译"""
    tool = AITools()
    result = tool.chat(
        f"把以下内容翻译成{to_lang}，只输出翻译结果，不要解释：\n\n{text}",
        system="你是一个专业翻译助手，输出简洁准确的翻译结果。"
    )
    print(result)


def cmd_summarize(text: str, style: str = "简短"):
    """文章总结"""
    tool = AITools()
    result = tool.chat(
        f"请{style}总结以下内容：\n\n{text}",
        system="你是一个文章总结助手，能够快速提取核心要点。"
    )
    print(result)


def cmd_polish(text: str):
    """润色优化"""
    tool = AITools()
    result = tool.chat(
        f"请润色优化以下文本，提升表达质量：\n\n{text}",
        system="你是一个专业写作润色助手，提升文本的表达质量和可读性。"
    )
    print(result)


def cmd_qa(context: str, question: str):
    """问答"""
    tool = AITools()
    result = tool.chat(
        f"根据以下背景信息回答问题。\n\n背景：\n{context}\n\n问题：{question}",
        system="你是一个知识问答助手，基于提供的背景信息准确回答问题。"
    )
    print(result)


def cmd_code_review(code: str):
    """代码审查"""
    tool = AITools()
    result = tool.chat(
        f"请审查以下代码，指出问题并提供改进建议：\n\n`\n{code}\n`",
        system="你是一个资深代码审查专家，帮助发现代码问题、提升质量和安全性。"
    )
    print(result)


def cmd_batch(input_file: str, operation: str, output: str = None):
    """批量处理"""
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    tool = AITools()
    results = []
    for i, line in enumerate(lines, 1):
        print(f"处理 {i}/{len(lines)}...", end="\r")
        if operation == "translate":
            r = tool.chat(f"翻译：{line}", system="只输出翻译结果")
        elif operation == "summarize":
            r = tool.chat(f"总结：{line}", system="简短总结")
        elif operation == "polish":
            r = tool.chat(f"润色：{line}", system="只输出润色结果")
        else:
            r = tool.chat(line)
        results.append(r)

    out = output or input_file.replace(".txt", f"_{operation}.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(f"\n✅ 完成，{len(results)} 条，结果保存到 {out}")


def main():
    parser = argparse.ArgumentParser(description="🤖 AI Tools - 命令行 AI 瑞士军刀")
    sub = parser.add_subparsers(dest="cmd")

    p = sub.add_parser("translate", help="翻译")
    p.add_argument("text", nargs="?", help="要翻译的文本")
    p.add_argument("-f", "--file", help="从文件读取")
    p.add_argument("-from", dest="from_lang", default="auto", help="源语言")
    p.add_argument("-to", dest="to_lang", default="中文", help="目标语言")

    p = sub.add_parser("summarize", help="总结")
    p.add_argument("text", nargs="?", help="要总结的内容")
    p.add_argument("-f", "--file", help="从文件读取")
    p.add_argument("-s", "--style", default="简短", help="总结风格")

    p = sub.add_parser("polish", help="润色")
    p.add_argument("text", nargs="?", help="要润色的文本")
    p.add_argument("-f", "--file", help="从文件读取")

    p = sub.add_parser("qa", help="问答")
    p.add_argument("-c", "--context", required=True, help="背景信息")
    p.add_argument("-q", "--question", required=True, help="问题")

    p = sub.add_parser("review", help="代码审查")
    p.add_argument("-f", "--file", required=True, help="代码文件")

    p = sub.add_parser("batch", help="批量处理")
    p.add_argument("-f", "--file", required=True, help="输入文件（每行一个）")
    p.add_argument("-o", "--op", dest="operation", required=True,
                   choices=["translate", "summarize", "polish"], help="操作类型")
    p.add_argument("-out", "--output", help="输出文件")

    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        return

    text = args.text
    if hasattr(args, "file") and args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    if not text and args.cmd not in ["qa", "batch", "review"]:
        print("错误：需要提供文本或文件")
        return

    try:
        if args.cmd == "translate":
            cmd_translate(text, getattr(args, "from_lang", "auto"), args.to_lang)
        elif args.cmd == "summarize":
            cmd_summarize(text, args.style)
        elif args.cmd == "polish":
            cmd_polish(text)
        elif args.cmd == "qa":
            cmd_qa(args.context, args.question)
        elif args.cmd == "review":
            with open(args.file, "r", encoding="utf-8") as f:
                cmd_code_review(f.read())
        elif args.cmd == "batch":
            cmd_batch(args.file, args.operation, args.output)
    except Exception as e:
        print(f"❌ 错误：{e}")


if __name__ == "__main__":
    main()