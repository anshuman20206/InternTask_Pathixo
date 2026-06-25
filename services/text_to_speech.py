import os
from gtts import gTTS


# Folder to store generated audio
AUDIO_DIR = "audio"
AUDIO_FILE = "response.mp3"


def text_to_speech(text: str) -> str:
    """
    Converts text to speech and saves it as response.mp3.

    Args:
        text (str): Text to convert into speech.

    Returns:
        str: Path to the generated audio file.
    """

    if not text:
        return None

    try:
        # Create audio directory if it doesn't exist
        os.makedirs(AUDIO_DIR, exist_ok=True)

        filepath = os.path.join(AUDIO_DIR, AUDIO_FILE)

        # Remove previous audio if it exists
        if os.path.exists(filepath):
            os.remove(filepath)

        # Generate speech
        tts = gTTS(
            text=text,
            lang="en",
            slow=False
        )

        # Save audio
        tts.save(filepath)

        return filepath

    except Exception as e:
        print(f"Text-to-Speech Error: {e}")
        return None