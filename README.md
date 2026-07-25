# 🎙️ MediaMind AI – Intelligent Media Analysis Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenAI-Whisper-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Mistral_AI-LLM-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Sarvam_AI-Speech_AI-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-blueviolet?style=for-the-badge">
</p>

---

# 📌 Project Overview

**MediaMind AI** is an AI-powered Media Intelligence Platform that transforms audio and video recordings into meaningful insights.

Upload **MP3, MP4, WAV, or M4A** media files to automatically generate accurate transcripts, meeting titles, executive summaries, action items, key decisions, and open questions. The application also includes a Retrieval-Augmented Generation (RAG) chatbot, enabling users to ask contextual questions and explore their uploaded media using natural language.

The project demonstrates an end-to-end Generative AI workflow by combining Speech-to-Text, Large Language Models (LLMs), Vector Databases, Retrieval-Augmented Generation (RAG), and an interactive Streamlit interface.

---

# 🚀 Features

- 📁 Upload audio and video recordings
- 🎙️ Automatic Speech-to-Text transcription using OpenAI Whisper
- 📝 AI-generated executive summaries
- 🏷️ Automatic meeting title generation
- ✅ Action Item extraction
- 📌 Key Decision identification
- ❓ Open Question extraction
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered conversational chatbot using RAG
- 🌐 Interactive Streamlit Web Application
- ⚡ Supports MP3, MP4, WAV and M4A formats

---

# 🏗️ System Architecture

```text
             Audio / Video Upload
      (MP3 • MP4 • WAV • M4A)
                    │
                    ▼
        Audio Processing & Chunking
          (FFmpeg + Pydub)
                    │
                    ▼
      Whisper Speech-to-Text Model
                    │
                    ▼
          Transcript Generation
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   Mistral AI              Embeddings
        │                       │
        ▼                       ▼
Meeting Title            ChromaDB Vector Store
Executive Summary               │
Action Items                    │
Key Decisions                   │
Open Questions                  │
        └───────────┬───────────┘
                    ▼
          LangChain RAG Pipeline
                    │
                    ▼
         AI Chat with Your Media
```

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.11

## AI & Machine Learning

- OpenAI Whisper
- Mistral AI
- Sarvam AI
- LangChain
- Prompt Engineering

## Vector Database

- ChromaDB

## Audio Processing

- FFmpeg
- Pydub

## Frontend

- Streamlit

## Backend

- Python

## Environment Management

- Python Virtual Environment
- dotenv

---

# 📂 Project Structure

```text
MediaMind-AI/
│
├── app.py
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarizer.py
│   ├── transcriber.py
│   └── vector_store.py
│
├── utils/
│   ├── audio_processor.py
│   ├── main.py
│   └── test.py
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Kedar14-byte/MediaMind-AI.git
```

Move into the project

```bash
cd MediaMind-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
MISTRAL_API_KEY=your_api_key
SARVAM_API_KEY=your_api_key

WHISPER_MODEL=small
SARVAM_STT_MODEL=saaras:v2.5
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser at

```
http://localhost:8501
```

---

# 💡 Workflow

1. Upload an audio or video recording.
2. Audio is processed and converted into supported formats.
3. Media is divided into manageable chunks.
4. Whisper converts speech into text.
5. Mistral AI generates:
   - Meeting Title
   - Executive Summary
   - Action Items
   - Key Decisions
   - Open Questions
6. Transcript embeddings are stored in ChromaDB.
7. LangChain retrieves relevant transcript chunks.
8. Ask questions about your uploaded media using the RAG chatbot.

---

# 📸 Application Preview

## 🏠 Home Page

> Add screenshot

---

## 📝 Executive Summary

> Add screenshot

---

## 🤖 AI Chat

> Add screenshot

---

# 🔮 Future Enhancements

- Speaker diarization
- Multi-language transcription
- PDF meeting reports
- Export to DOCX/PDF
- Timestamp navigation
- Meeting analytics dashboard
- Authentication & user accounts
- Cloud storage integration
- Audio sentiment analysis

---

# 🎯 Skills Demonstrated

- Python
- Generative AI
- Prompt Engineering
- LangChain
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- ChromaDB
- OpenAI Whisper
- Mistral AI
- Sarvam AI
- Speech-to-Text
- Streamlit
- REST API Integration
- Environment Variable Management
- Git & GitHub

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Kedar Sankpal**

- GitHub: https://github.com/Kedar14-byte
- LinkedIn: https://www.linkedin.com/in/kedar-sankpal14/

---

## ⭐ If you found this project useful, please consider giving it a Star!