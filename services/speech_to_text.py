import os
import tempfile
import whisper
import subprocess

# Load Whisper model only once
# Options: tiny, base, small, medium, large
model = whisper.load_model("small")


def transcribe_audio(audio_bytes):
    """
    Transcribes microphone audio using a local Whisper model.

    Args:
        audio_bytes (bytes): Audio bytes from streamlit-mic-recorder.

    Returns:
        str: Transcribed text.
    """

    if audio_bytes is None:
        return None

    webm_path = None
    wav_path = None

    try:
        # Save browser audio (WebM)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as webm_file:
            webm_file.write(audio_bytes)
            webm_path = webm_file.name

        # Temporary WAV path
        wav_path = webm_path.replace(".webm", ".wav")

        # Convert WebM → WAV using FFmpeg
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                webm_path,
                "-ar",
                "16000",
                "-ac",
                "1",
                wav_path,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )

        # Transcribe
        result = model.transcribe(
            wav_path,
            language="en",
            fp16=False,
            temperature=0,
            beam_size=5,
            best_of=5,
        )

        return result["text"].strip()

    except Exception as e:
        print(f"Whisper Error: {e}")
        return None

    finally:
        if webm_path and os.path.exists(webm_path):
            os.remove(webm_path)

        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)