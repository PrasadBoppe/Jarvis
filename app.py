from core.llm import LLM
from core.session import ChatSession
import time
from voice.text_to_speech import TextToSpeech
from voice.speech_to_text import SpeechToText

def main():
    llm = LLM()
    session = ChatSession()
    tts = TextToSpeech()
    stt = SpeechToText()

    print("=" * 40)
    print("🤖 Jarvis")
    print("Say 'exit' to quit.")
    print("=" * 40)

    while True:
        user_input = stt.listen()
        print(f"You: {user_input}")

        if not user_input:
            print("Didn't hear anything.")
            continue

        if user_input.lower() == "clear":
            session.clear()
            print("Conversation cleared.")
            continue

        if user_input.lower() == "exit":
            break

        command = (
            user_input
            .strip()
            .lower()
            .rstrip(".,!?")
        )

        if command == "exit":
            break

        session.add_user_message(user_input)

        start = time.perf_counter()

        reply = llm.ask(session.messages)

        session.add_assistant_message(reply)

        elapsed = time.perf_counter() - start

        print(f"\nJarvis: {reply}")
        tts.speak(reply)
        
        print(f"\n⏱️ {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()