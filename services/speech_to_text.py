import os
import tempfile
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def transcribe_audio(audio_bytes):
    """
    Transcribes microphone audio using Groq Whisper API.

    Args:
        audio_bytes (bytes): Audio bytes from streamlit-mic-recorder.

    Returns:
        str: Transcribed text or None.
    """

    if audio_bytes is None:
        return None

    temp_audio = None

    try:
        # Save the recorded audio as a temporary WebM file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as f:
            f.write(audio_bytes)
            temp_audio = f.name

        # Send audio to Groq Whisper
        with open(temp_audio, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                language="en",
                temperature=0,
                response_format="verbose_json",
            )

        return transcription.text.strip()

    except Exception as e:
        print(f"Groq STT Error: {e}")
        return None

    finally:
        if temp_audio and os.path.exists(temp_audio):
            os.remove(temp_audio)