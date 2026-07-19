from config import SYSTEM_PROMPT, MAX_HISTORY


class ChatSession:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

    def add_user_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )
        self._trim_history()

    def add_assistant_message(self, message: str) -> None:
        self.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )
        self._trim_history()

    def _trim_history(self) -> None:
        """Keep only the most recent messages, excluding the system prompt."""
        if len(self.messages) > MAX_HISTORY + 1:  # +1 for system prompt
            # Keep system prompt + last MAX_HISTORY messages
            self.messages = [self.messages[0]] + self.messages[-MAX_HISTORY:]

    def clear(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]