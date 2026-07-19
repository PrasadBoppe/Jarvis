import subprocess


class TextToSpeech:
    def speak(self, text: str) -> None:
        """Speak the given text using the macOS speech engine."""
        subprocess.run(["say", text], check=False)