# 🎬 AI Video Assistant with RAG

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenAI-Whisper-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-blueviolet?style=for-the-badge">
</p>

## 📌 Project Overview

AI Video Assistant is an end-to-end Generative AI application that transforms long videos into actionable insights.

The application accepts a YouTube URL or a local audio/video file, transcribes the content using OpenAI Whisper, summarizes the discussion using Large Language Models (LLMs), extracts important action items and key decisions, and enables users to ask questions about the content using Retrieval-Augmented Generation (RAG).

This project demonstrates the practical integration of Speech-to-Text, NLP, Vector Databases, LangChain, and Streamlit into a single AI-powered application.

---

## 🚀 Features

- 🎥 Process YouTube videos
- 📁 Upload local audio/video files
- 🎙️ Speech-to-Text transcription using Whisper
- 📝 AI-generated meeting summaries
- ✅ Automatic Action Item extraction
- 📌 Key Decision extraction
- ❓ Open Question identification
- 🔍 Semantic Search using ChromaDB
- 🤖 Chat with your video using RAG
- 🌐 Interactive Streamlit Web Application

---

# 🏗️ System Architecture

```
                YouTube URL / Local Video
                           │
                           ▼
                 Audio Extraction (yt-dlp)
                           │
                           ▼
                  Audio Chunking (Pydub)
                           │
                           ▼
              Whisper Speech-to-Text Model
                           │
                           ▼
                  Transcript Generation
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
     AI Summarizer                  Vector Embeddings
          │                                 │
          ▼                                 ▼
 Action Items / Decisions            ChromaDB Vector Store
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                 LangChain RAG Pipeline
                         │
                         ▼
                Chat With Your Meeting
```

---

# 🛠️ Tech Stack

### Programming Language

- Python 3.11

### AI / LLM

- OpenAI Whisper
- LangChain
- OpenAI / Google Gemini (depending on configuration)

### Vector Database

- ChromaDB

### NLP

- Whisper Speech Recognition
- Prompt Engineering

### Backend

- Python

### Frontend

- Streamlit

### Audio Processing

- yt-dlp
- FFmpeg
- Pydub

### Environment

- Python Virtual Environment
- dotenv

---

# 📂 Project Structure

```
AI-Video-Assistant/
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
├── .env
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Kedar14-byte/AI-Video-Assistant.git
```

Go inside the project

```bash
cd AI-Video-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

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

Example

```text
OPENAI_API_KEY=your_api_key
```

or

```text
GOOGLE_API_KEY=your_api_key
```

depending on the model you are using.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application will open at

```
http://localhost:8501
```

---

# 💡 How It Works

1. User enters a YouTube URL or uploads a local video/audio file.
2. Audio is extracted using yt-dlp.
3. Audio is divided into chunks using Pydub.
4. Whisper converts speech into text.
5. The transcript is summarized using an LLM.
6. Action items, key decisions, and questions are extracted.
7. Transcript embeddings are stored in ChromaDB.
8. LangChain retrieves relevant chunks.
9. Users can chat with the meeting using RAG.

---

# 📸 Demo

### Home Page

> Add a screenshot here

### Summary

> Add a screenshot here

### Chat Interface

> Add a screenshot here

---

# Future Improvements

- Speaker diarization
- Multi-language transcription
- PDF report generation
- Meeting analytics dashboard
- Cloud deployment
- User authentication
- Audio sentiment analysis
- Timestamp-based transcript navigation

---

# Skills Demonstrated

- Python
- Generative AI
- Prompt Engineering
- LangChain
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Vector Embeddings
- OpenAI Whisper
- Speech-to-Text
- Streamlit
- REST API Integration
- Environment Variable Management
- Git & GitHub

---

# License

This project is licensed under the MIT License.

---

# Author

**Kedar Sankpal**

- GitHub: https://github.com/Kedar14-byte
- LinkedIn: https://www.linkedin.com/in/kedar-sankpal14/

---

## ⭐ If you found this project useful, please consider giving it a Star!
