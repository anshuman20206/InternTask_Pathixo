import os
import streamlit as st
from streamlit_mic_recorder import mic_recorder

from services.speech_to_text import transcribe_audio
from services.llm_service import generate_response
from services.text_to_speech import text_to_speech


# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Pathixo Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)

# -------------------- LOAD CSS --------------------

css_file = "assets/styles.css"

if os.path.exists(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------

if "user_text" not in st.session_state:
    st.session_state.user_text = ""

if "ai_response" not in st.session_state:
    st.session_state.ai_response = ""

if "audio_path" not in st.session_state:
    st.session_state.audio_path = None

# -------------------- HEADER --------------------

st.markdown(
    """
    <h1 style='text-align:center;'>
         Voice AI Assistant
    </h1>
    <p style='text-align:center;color:gray;'>
        Speak naturally and receive an AI-generated voice response.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------- TWO COLUMN LAYOUT --------------------

left, right = st.columns(2)

# =====================================================
# LEFT CARD
# =====================================================

with left:

    st.subheader(" Speak")

    audio = mic_recorder(
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop Recording",
        just_once=True,
        use_container_width=True,
        key="voice_recorder",
    )

    if audio:

        with st.spinner("Transcribing your voice..."):

            user_text = transcribe_audio(audio["bytes"])

            st.session_state.user_text = user_text

        if user_text:

            with st.spinner("Thinking..."):

                response = generate_response(user_text)

                st.session_state.ai_response = response

            with st.spinner("Generating voice..."):

                audio_path = text_to_speech(response)

                st.session_state.audio_path = audio_path

# =====================================================
# RIGHT CARD
# =====================================================

with right:

    st.subheader("AI Response")

    st.markdown("### 🗣️ You Said")

    if st.session_state.user_text:

        st.info(st.session_state.user_text)

    else:

        st.write("Waiting for your voice input...")

    st.markdown("---")

    st.markdown("### 💬 Assistant")

    if st.session_state.ai_response:

        st.success(st.session_state.ai_response)

    else:

        st.write("AI response will appear here.")

    # -------------------- AUDIO --------------------

    if st.session_state.audio_path:

        with open(st.session_state.audio_path, "rb") as audio_file:

            st.audio(
                audio_file.read(),
                format="audio/mp3",
                autoplay=True
            )

st.divider()

st.caption("Built with ❤️ using Streamlit • Whisper • Groq • gTTS")