MODEL = "llama3.2:3b"

SYSTEM_PROMPT = (
    "You are Jarvis. "
    "Be concise. "
    "Answer in plain text. "
    "Keep responses under 80 words unless the user asks for more."
)

MAX_HISTORY = 10

# Audio recording configuration
SAMPLE_RATE = 16000
CHUNK_DURATION = 0.1      # seconds
SILENCE_THRESHOLD = 500   # we'll tune this later
SILENCE_DURATION = 1.0    # seconds before stopping
MIN_SPEECH_DURATION = 0.5  # minimum speech duration to avoid garbage transcriptions