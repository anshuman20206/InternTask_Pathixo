# 🎙️ Voice-Based AI Assistant

A simple, fast, and intelligent voice-based AI assistant built with **Python**, **Streamlit**, **Groq Whisper API**, **Groq Llama 3.3**, and **gTTS**.

The application records audio from the user's microphone, transcribes speech using the **Groq Whisper API**, generates intelligent responses using **Groq's Llama 3.3 70B Versatile** model, converts the response back into speech, and automatically plays the generated audio.

---

## 🚀 Features

- 🎤 Record voice directly from the browser
- 📝 Accurate Speech-to-Text using **Groq Whisper API**
- 🤖 AI-powered responses using **Groq Llama 3.3 70B Versatile**
- 🔊 Text-to-Speech using **Google Text-to-Speech (gTTS)**
- ▶️ Automatic audio playback
- 💬 Clean and responsive Streamlit interface
- ⚡ Fast cloud-based speech recognition
- ☁️ No local AI models or GPU required

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Voice Recording | streamlit-mic-recorder |
| Speech-to-Text | Groq Whisper API |
| Large Language Model | Groq (Llama 3.3 70B Versatile) |
| Text-to-Speech | gTTS |
| Environment Variables | python-dotenv |

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
git clone https://github.com/anshuman20206/InternTask_Pathixo.git
cd InternTask_Pathixo
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create a `.env` File

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will automatically open in your default browser.

---

## 🔄 Application Workflow

```text
🎤 User Speaks
        │
        ▼
Microphone Recording
        │
        ▼
Groq Whisper API
(Speech-to-Text)
        │
        ▼
User Query
        │
        ▼
Groq Llama 3.3 70B
(Response Generation)
        │
        ▼
Generated Response
        │
        ▼
gTTS
(Text-to-Speech)
        │
        ▼
🔊 Audio Playback
```

---

## 📦 Requirements

- Python 3.10+
- Internet connection
- Groq API Key

> **Note:** Since speech recognition is handled by the Groq Whisper API, **FFmpeg, Torch, Torchaudio, and local Whisper models are no longer required.**

---

## 🤖 AI Models Used

### Speech-to-Text

```
whisper-large-v3
```

via the Groq API.

### Large Language Model

```
llama-3.3-70b-versatile
```

via the Groq API.

---

## 📸 User Interface

The application provides a simple two-panel layout.

### Left Panel

- 🎤 Voice recording button
- 📝 Live transcribed user speech

### Right Panel

- 🤖 AI-generated response
- 🔊 Automatic audio playback

---

## ✨ Advantages of Using Groq Whisper API

- Faster than running Whisper locally
- Higher transcription accuracy
- No GPU required
- No FFmpeg installation
- No Torch dependency
- Lower memory usage
- Simple deployment

---

## 📌 Future Improvements

- 💬 Multi-turn conversation memory
- 🌍 Multi-language support
- 🎙️ Voice selection
- ⚡ Streaming AI responses
- 📄 Chat history
- 🔉 Better Text-to-Speech (Edge-TTS)
- 📥 Download conversation audio
- 📱 Mobile-friendly interface

---

## 👨‍💻 Author

**Anshuman Singh**

B.Tech Computer Science Engineering

AI & Full Stack Developer

- GitHub: https://github.com/anshuman20206
- LinkedIn: https://www.linkedin.com/in/anshumansinghsdd

---

## 📄 License

This project was developed as part of the **Pathixo AI Internship Assignment** and is intended for educational and demonstration purposes.