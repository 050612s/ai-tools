#!/usr/bin/env python3
"""
AI Tools - LLM API 客户端
支持 SiliconFlow、OpenAI 兼容接口
"""
import os
import requests
from typing import List, Dict

class AIClient:
    def __init__(self):
        # 优先使用 SiliconFlow
        self.api_key = os.environ.get("SILICONFLOW_API_KEY") or os.environ.get("OPENAI_API_KEY")
        self.base_url = os.environ.get("SILICONFLOW_BASE_URL") or os.environ.get("OPENAI_BASE_URL") or "https://api.siliconflow.cn/v1"
        self.model = os.environ.get("AI_MODEL", "Qwen/Qwen2.5-7B-Instruct")

        if not self.api_key:
            print("⚠️  警告: 未设置 API_KEY，部分功能可能不可用")
            print("   请设置 SILICONFLOW_API_KEY 或 OPENAI_API_KEY 环境变量")

    def _call(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        """调用 LLM API"""
        if not self.api_key:
            return "❌ 错误: 未配置 API Key\n请设置 SILICONFLOW_API_KEY 或 OPENAI_API_KEY 环境变量"

        url = f"{self.base_url.rstrip('/')}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"❌ 网络错误: {e}"

    def translate(self, text: str, source: str = "auto", target: str = "zh") -> str:
        """翻译文本"""
        lang_map = {"zh": "中文", "en": "英文", "ja": "日文", "ko": "韩文", "fr": "法文", "de": "德文"}
        target_name = lang_map.get(target, target)
        prompt = f"""你是一个专业翻译。请将以下文本翻译成{target_name}，只输出翻译结果，不要解释：

{text}"""
        return self._call([{"role": "user", "content": prompt}]).strip()

    def summarize(self, text: str, max_length: int = 200) -> str:
        """总结文本"""
        prompt = f"""你是一个文章总结助手。请用简洁的语言总结以下内容，控制在 {max_length} 字以内：

{text}"""
        return self._call([{"role": "user", "content": prompt}], temperature=0.3)

    def polish(self, text: str) -> str:
        """润色文本"""
        prompt = f"""你是一个文字润色专家。请优化以下文本，使其更流畅、专业、有吸引力。只输出润色结果：

{text}"""
        return self._call([{"role": "user", "content": prompt}], temperature=0.7)

    def ask(self, question: str) -> str:
        """问答"""
        prompt = f"""你是一个知识渊博的助手。请简洁、准确地回答以下问题：

{question}"""
        return self._call([{"role": "user", "content": prompt}], temperature=0.7)

    def generate_title(self, content: str) -> str:
        """生成标题"""
        prompt = f"""你是一个标题创作专家。请为以下内容生成3个吸引人的标题（用换行分隔）：

{content}"""
        return self._call([{"role": "user", "content": prompt}], temperature=0.8, max_tokens=300)

    def extract_keywords(self, text: str, top_n: int = 5) -> str:
        """提取关键词"""
        prompt = f"""从以下文本中提取 {top_n} 个核心关键词，用逗号分隔，只输出关键词：

{text}"""
        return self._call([{"role": "user", "content": prompt}], temperature=0.3)

    def chat(self, messages: List[Dict]) -> str:
        """对话"""
        return self._call(messages, temperature=0.8)
