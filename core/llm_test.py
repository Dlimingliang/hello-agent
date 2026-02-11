from dotenv import load_dotenv

from core.llm import HelloAgentsLLM


def main() -> None:
    load_dotenv()

    llm = HelloAgentsLLM()

    # 准备消息
    messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]

    # 注意：`HelloAgentsLLM.chat()` 是一个 generator（流式输出）。
    # 只有开始迭代它时，才会真正发起 LLM 请求。
    for chunk in llm.chat(messages):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
