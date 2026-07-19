from ollama import chat
from config import MODEL

class LLM:
    def ask(self, messages: list):
        stream = chat(
            model=MODEL,
            messages=messages,
            stream=True,
            think=False,
        )

        full_response = ""

        #print("\nJarvis: ", end="", flush=True)

        for chunk in stream:
            text = chunk.message.content
            #print(text, end="", flush=True)
            full_response += text

        #print()

        return full_response