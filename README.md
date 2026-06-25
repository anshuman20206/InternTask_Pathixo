# 🎙️ Voice-Based AI Assistant

A simple voice-based AI assistant built with **Python**, **Streamlit**, **Local Whisper**, **Groq LLM**, and **gTTS**. The application records audio from the user's microphone, converts speech to text using a locally running Whisper model, sends the transcription to Groq's LLM for response generation, converts the response back into speech, and automatically plays the generated audio.

---

## 🚀 Features

* 🎤 Record voice directly from the browser
* 📝 Speech-to-Text using Local Whisper
* 🤖 AI-powered responses using Groq Llama
* 🔊 Text-to-Speech using Google Text-to-Speech (gTTS)
* ▶️ Automatic audio playback
* 💬 Simple and clean Streamlit interface
* ⚡ Fast and lightweight architecture

---

## 🛠️ Tech Stack

| Component             | Technology                     |
| --------------------- | ------------------------------ |
| Frontend              | Streamlit                      |
| Voice Recording       | streamlit-mic-recorder         |
| Speech-to-Text        | OpenAI Whisper (Local)         |
| Large Language Model  | Groq (Llama 3.3 70B Versatile) |
| Text-to-Speech        | gTTS                           |
| Environment Variables | python-dotenv                  |

---

## 📂 Project Structure

```text
PATHIXO-2/

│── app.py
│── .env
│── requirements.txt
│── README.md

├── assets/
│   └── styles.css

└── services/
    ├── speech_to_text.py
    ├── llm_service.py
    └── text_to_speech.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd PATHIXO-2
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install FFmpeg

Whisper requires FFmpeg.

Verify installation:

```bash
ffmpeg -version
```

---

### 4. Create Environment File

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 🔄 Application Workflow

1. User records audio through the microphone.
2. Audio is saved as a temporary WAV file.
3. Local Whisper transcribes speech into text.
4. The transcribed text is sent to the Groq LLM.
5. Groq generates an AI response.
6. gTTS converts the response into speech.
7. The generated audio is automatically played back.
8. Both the user's transcription and AI response are displayed on the interface.

---

## 📦 Requirements

* Python 3.10+
* FFmpeg
* Internet connection (required for Groq API and gTTS)

---

## 🤖 LLM Model

This project uses:

```
llama-3.3-70b-versatile
```

via the Groq API.

---

## 📸 User Interface

The application contains a simple two-panel layout:

* **Left Panel**

  * Voice recording button
  * Transcribed user speech

* **Right Panel**

  * AI-generated response
  * Automatic audio playback

---

## 📌 Future Improvements

* Conversation history
* Chat memory
* Multiple language support
* Streaming responses
* Voice selection
* Offline Text-to-Speech
* Download generated audio

---

## 👨‍💻 Author

**Anshuman Singh**

B.Tech Computer Science Engineering

AI & Full Stack Developer

GitHub: https://github.com/anshuman20206
