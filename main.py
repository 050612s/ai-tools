#!/usr/bin/env python3
"""
AI Tools - 命令行 AI 工具箱
支持翻译、总结、润色、问答、标题生成、关键词提取
"""
import os
import sys
import argparse
import json
from api_client import AIClient

def main():
    parser = argparse.ArgumentParser(
        description="🤖 AI Tools - 命令行 AI 工具箱",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  %(prog)s translate "Hello world"
  %(prog)s summarize < article.txt
  %(prog)s polish "原始文本内容"
  %(prog)s ask "什么是人工智能？"
  %(prog)s title "文章正文内容..."
  %(prog)s keywords "要提取关键词的文本内容"
  %(prog)s chat
        """
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # 翻译
    p_trans = sub.add_parser("translate", help="翻译文本")
    p_trans.add_argument("text", nargs="+", help="要翻译的文本")
    p_trans.add_argument("-s", "--source", default="auto", help="源语言 (默认: auto)")
    p_trans.add_argument("-t", "--target", default="zh", help="目标语言 (默认: zh)")

    # 总结
    sub.add_parser("summarize", help="总结文本").add_argument("text", nargs="+", help="要总结的文本")

    # 润色
    sub.add_parser("polish", help="润色文本").add_argument("text", nargs="+", help="要润色的文本")

    # 问答
    sub.add_parser("ask", help="问答").add_argument("text", nargs="+", help="要提问的内容")

    # 标题生成
    sub.add_parser("title", help="生成标题").add_argument("text", nargs="+", help="文章正文内容")

    # 关键词提取
    sub.add_parser("keywords", help="提取关键词").add_argument("text", nargs="+", help="要处理的文本")

    # 对话模式
    sub.add_parser("chat", help="进入对话模式")

    args = parser.parse_args()
    client = AIClient()

    text = " ".join(args.text) if hasattr(args, "text") and args.text else None

    if args.command == "translate":
        result = client.translate(text, source=args.source, target=args.target)
        print(result)

    elif args.command == "summarize":
        result = client.summarize(text)
        print("📋 摘要结果：")
        print(result)

    elif args.command == "polish":
        result = client.polish(text)
        print("✨ 润色结果：")
        print(result)

    elif args.command == "ask":
        result = client.ask(text)
        print(result)

    elif args.command == "title":
        result = client.generate_title(text)
        print("📰 建议标题：")
        print(result)

    elif args.command == "keywords":
        result = client.extract_keywords(text)
        print("🔑 关键词：")
        print(result)

    elif args.command == "chat":
        print("💬 AI 对话模式（输入 quit 退出）")
        print("-" * 40)
        messages = []
        while True:
            try:
                user_input = input("你: ")
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("再见！👋")
                    break
                if not user_input.strip():
                    continue
                messages.append({"role": "user", "content": user_input})
                response = client.chat(messages)
                print(f"AI: {response}")
                messages.append({"role": "assistant", "content": response})
            except (KeyboardInterrupt, EOFError):
                print("\n再见！👋")
                break

if __name__ == "__main__":
    main()
