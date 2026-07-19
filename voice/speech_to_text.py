import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from mlx_whisper import transcribe
from config import SAMPLE_RATE, CHUNK_DURATION, SILENCE_THRESHOLD, SILENCE_DURATION

class SpeechToText:
    DURATION = 5  # seconds

    def listen(self) -> str:
        """Record audio and return the recognized text."""
        self._record_until_silence()
        return self._transcribe()

    def _record_until_silence(self) -> None:
        """Record audio chunks until silence is detected using two-state machine."""
        WAITING = "WAITING"
        RECORDING = "RECORDING"
        
        print("\n🎤 Listening...")

        chunk_size = int(SAMPLE_RATE * CHUNK_DURATION)
        silence_chunks = int(SILENCE_DURATION / CHUNK_DURATION)

        state = WAITING
        chunks = []
        silent_count = 0

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
        ) as stream:

            while True:
                chunk, _ = stream.read(chunk_size)

                if state == WAITING:
                    if not self._is_silent(chunk):
                        print("🗣️ Speech detected")
                        state = RECORDING
                        chunks.append(chunk)
                else:  # RECORDING
                    chunks.append(chunk)
                    
                    if self._is_silent(chunk):
                        silent_count += 1
                    else:
                        silent_count = 0

                    if silent_count >= silence_chunks:
                        print("🤫 Silence detected")
                        break

        audio = np.concatenate(chunks, axis=0)

        write("recording.wav", SAMPLE_RATE, audio)

        print("✅ Recording saved.")

    def _is_silent(self, chunk) -> bool:
        """Check if the audio chunk is below the silence threshold."""
        return abs(chunk).max() < SILENCE_THRESHOLD

    def _transcribe(self) -> str:
        """Transcribe the audio file and return the text."""
        result = transcribe(
            "recording.wav",
            path_or_hf_repo="mlx-community/whisper-tiny"
        )

        print(result["text"])

        return result["text"].strip()