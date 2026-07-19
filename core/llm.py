from ollama import chat


class LLM:
    def ask(self, message: str) -> str:
        response = chat(
            model="qwen3:4b",
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response.message.content