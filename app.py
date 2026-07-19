from core.llm import LLM
import time

def main():
    llm = LLM()

    print("=" * 40)
    print("🤖 Jarvis")
    print("Type 'exit' to quit.")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        start = time.perf_counter()

        reply = llm.ask(user_input)

        elapsed = time.perf_counter() - start

        print(f"\n⏱️ {elapsed:.2f} seconds")
        print(f"\nJarvis: {reply}")


if __name__ == "__main__":
    main()