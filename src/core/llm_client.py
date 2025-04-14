from openai import OpenAI
from config.settings import *

# 初始化客户端
client = OpenAI(
    api_key=api_key,  # 替换为你的 API 密钥
    base_url="https://api.siliconflow.cn/v1"  # 替换为硅基流动的实际 API 地址
)

def query_llm(prompt, model=model):
    """
    调用硅基流动 LLM API 生成响应（非流式返回）
    :param prompt: 用户输入的提示
    :param model: 使用的模型名称
    :return: LLM 的完整响应
    """
    try:
        # 调用 chat.completions 接口（非流式返回）
        response = client.chat.completions.create(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=False  # 禁用流式输出
        )

        # 处理完整响应
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content  # 使用点操作符访问属性
        else:
            return "未收到有效的响应内容。"
    except Exception as e:
        return f"调用 LLM API 时出错: {e}"
