import time
from ollama import chat

start = time.perf_counter()

response = chat(
    model="qwen3:4b",
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

elapsed = time.perf_counter() - start

print(response.message.content)
print(f"\nTime: {elapsed:.2f}s")