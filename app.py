import time
import streamlit as st
from dotenv import load_dotenv

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediaMind AI",
    page_icon="🎙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #111118;
    --surface-2: #1a1a25;
    --border: #2a2a3a;
    --accent: #7c3aed;
    --accent-glow: #9f67ff;
    --accent-2: #06b6d4;
    --text: #e8e8f0;
    --text-muted: #7070a0;
    --success: #10b981;
}

html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

.stApp { background: var(--bg) !important; }

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * { color: var(--text) !important; }

h1, h2, h3, h4, h5, h6 { font-family: 'Syne', sans-serif !important; color: var(--text) !important; }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, var(--accent-glow) 50%, var(--accent-2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--text-muted);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, var(--accent), var(--accent-2));
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
}

.card-content { font-size: 0.875rem; line-height: 1.7; color: var(--text); }

.badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.badge-purple { background: rgba(124,58,237,0.2); color: var(--accent-glow); border: 1px solid rgba(124,58,237,0.3); }
.badge-cyan   { background: rgba(6,182,212,0.15); color: var(--accent-2); border: 1px solid rgba(6,182,212,0.3); }
.badge-green  { background: rgba(16,185,129,0.15); color: var(--success); border: 1px solid rgba(16,185,129,0.3); }

.status-bar {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    background: var(--surface-2);
    border-radius: 8px;
    margin: 0.4rem 0;
    border: 1px solid var(--border);
    font-size: 0.8rem;
}

.status-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.dot-active   { background: var(--accent-glow); box-shadow: 0 0 8px var(--accent-glow); animation: pulse 1.5s infinite; }
.dot-done     { background: var(--success); }
.dot-pending  { background: var(--border); }

@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

.transcript-box {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.25rem;
    font-size: 0.82rem;
    line-height: 1.8;
    max-height: 300px;
    overflow-y: auto;
    color: var(--text-muted);
    white-space: pre-wrap;
}

/* ==========================================
   INPUTS & BUTTONS PURPLE HOVER STYLING
   ========================================== */

/* File Uploader Container */
[data-testid="stFileUploader"] section {
    background-color: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease-in-out !important;
}

[data-testid="stFileUploader"] section:hover {
    border-color: var(--accent) !important;
    box-shadow: 0px 0px 12px rgba(124, 58, 237, 0.25) !important;
}

/* Internal Browse Button */
[data-testid="stFileUploader"] button {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: var(--accent) !important;
    color: #ffffff !important;
    border-color: var(--accent-glow) !important;
}

/* ==========================================
   SELECTBOX (LANGUAGE DROPDOWN) DARK OVERRIDE
   ========================================== */

/* 1. Target the outer Streamlit container */
.stSelectbox,
.stSelectbox > div,
.stSelectbox div[data-baseweb="select"],
.stSelectbox div[data-baseweb="select"] > div,
.stSelectbox div[data-baseweb="select"] * {
    background-color: var(--surface-2) !important;
    color: var(--text) !important;
}

/* 2. Style the border & rounded corners */
.stSelectbox div[data-baseweb="select"] > div {
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease-in-out !important;
}

/* 3. Hover state with purple glow */
.stSelectbox div[data-baseweb="select"] > div:hover {
    border-color: var(--accent) !important;
    box-shadow: 0px 0px 12px rgba(124, 58, 237, 0.25) !important;
}

/* 4. Dropdown Arrow & Text formatting */
.stSelectbox div[data-baseweb="select"] svg {
    fill: var(--text-muted) !important;
}

/* 5. Dropdown Popup List (When clicked open) */
ul[role="listbox"],
ul[role="listbox"] li {
    background-color: var(--surface-2) !important;
    color: var(--text) !important;
}
}

/* 4. Dropdown Arrow & Text formatting */
.stSelectbox div[data-baseweb="select"] svg {
    fill: var(--text-muted) !important;
}

/* 5. Dropdown Popup List (When clicked open) */
ul[role="listbox"],
ul[role="listbox"] li {
    background-color: var(--surface-2) !important;
    color: var(--text) !important;
}
/* Selectbox Dropdown (Language Input) */
div[data-baseweb="select"],
div[data-baseweb="select"] > div,
div[data-baseweb="select"] * {
    background-color: var(--surface-2) !important;
    color: var(--text) !important;
}

div[data-baseweb="select"] > div {
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease-in-out !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--accent) !important;
    box-shadow: 0px 0px 12px rgba(124, 58, 237, 0.25) !important;
}

div[data-baseweb="select"] svg {
    fill: var(--text-muted) !important;
}

/* Primary Sidebar Action Button */
div.stButton > button {
    background-color: var(--surface-2) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease-in-out !important;
}

div.stButton > button:hover {
    background-color: var(--accent) !important;
    color: #ffffff !important;
    border-color: var(--accent-glow) !important;
    box-shadow: 0px 0px 15px rgba(124, 58, 237, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Session State Init ──────────────────────────────────────────────────────────
for key, default in {
    "result": None,
    "chat_history": [],
    "pipeline_done": False,
    "pipeline_steps": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

def render_step_bar(label: str, key: str, icon: str):
    s = st.session_state.pipeline_steps.get(key, "pending")
    css = "dot-active" if s == "active" else ("dot-done" if s == "done" else "dot-pending")
    st.markdown(f"""
    <div class="status-bar">
        <div class="status-dot {css}"></div>
        <span>{icon} {label}</span>
    </div>""", unsafe_allow_html=True)

# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="hero-title" style="font-size:1.6rem">MediaMind AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">MEDIA INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown('<span class="badge badge-purple">Input Source</span>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Audio/Video", type=["mp3", "mp4", "wav", "m4a"])
    
    if uploaded_file:
        size_mb = uploaded_file.size / (1024 * 1024)
        st.caption(f"Selected: {uploaded_file.name} ({size_mb:.1f} MB)")

    language = st.selectbox("Language", ["English", "Hinglish"], index=0)
    run_btn = st.button("⚡  Analyze Media", use_container_width=True)

    if st.session_state.pipeline_done:
        st.markdown("---")
        st.markdown('<span class="badge badge-green">Pipeline Status</span>', unsafe_allow_html=True)
        for step, icon, label in [
            ("audio",      "🔊", "Audio Processing"),
            ("transcript", "📝", "Transcription"),
            ("title",      "🏷️", "Title Generation"),
            ("summary",    "📋", "Summarisation"),
            ("extract",    "🔍", "Extraction"),
            ("rag",        "🧠", "RAG Engine"),
        ]:
            render_step_bar(label, step, icon)

# ─── Main Area ──────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">MediaMind AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Your universal media intelligence engine.</div>', unsafe_allow_html=True)
st.markdown("---")

# ── Pipeline Execution ──────────────────────────────────────────────────────────
if run_btn:
    if not uploaded_file:
        st.error("Please upload an audio or video file first.")
    else:
        st.session_state.pipeline_done = False
        st.session_state.result = None
        st.session_state.chat_history = []
        st.session_state.pipeline_steps = {}

        progress_placeholder = st.empty()

        def update_step(key, state):
            st.session_state.pipeline_steps[key] = state

        try:
            with progress_placeholder.container():
                st.info("⚙️ Pipeline running — check sidebar for status…")

            update_step("audio", "active")
            chunks = process_input(uploaded_file)
            update_step("audio", "done")

            update_step("transcript", "active")
            transcript = transcribe_all(chunks, language.lower())
            update_step("transcript", "done")

            update_step("title", "active")
            title = generate_title(transcript)
            update_step("title", "done")

            update_step("summary", "active")
            summary = summarize(transcript)
            update_step("summary", "done")

            update_step("extract", "active")
            action_items = extract_action_items(transcript)
            decisions = extract_key_decisions(transcript)
            questions = extract_questions(transcript)
            update_step("extract", "done")

            update_step("rag", "active")
            rag_chain = build_rag_chain(transcript)
            update_step("rag", "done")

            st.session_state.result = {
                "title": title,
                "transcript": transcript,
                "summary": summary,
                "action_items": action_items,
                "key_decisions": decisions,
                "open_questions": questions,
                "rag_chain": rag_chain,
            }

            st.session_state.pipeline_done = True
            progress_placeholder.success("✅ Media analysis complete!")
            time.sleep(0.5)
            progress_placeholder.empty()
            st.rerun()

        except Exception as e:
            for k in ["audio", "transcript", "title", "summary", "extract", "rag"]:
                if st.session_state.pipeline_steps.get(k) == "active":
                    st.session_state.pipeline_steps[k] = "pending"
            progress_placeholder.error(f"❌ Error during execution: {e}")

# ── Output Results ──────────────────────────────────────────────────────────────
if st.session_state.result:
    r = st.session_state.result

    st.markdown(f"""
    <div class="card">
        <div class="card-title">📌 Session Title</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:700;color:var(--text)">
            {r['title']}
        </div>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="medium")
    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">📋 Summary</div>
            <div class="card-content">{r['summary']}</div>
        </div>""", unsafe_allow_html=True)

    with col2:
        with st.expander("📝 Full Transcript", expanded=False):
            st.markdown(f'<div class="transcript-box">{r["transcript"]}</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">✅ Action Items</div>
            <div class="card-content">{r['action_items']}</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">🔑 Key Decisions</div>
            <div class="card-content">{r['key_decisions']}</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">❓ Open Questions</div>
            <div class="card-content">{r['open_questions']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Interactive Chat Section
    st.markdown("### 💬 Chat with your Media")
    
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    with st.form("chat_form", clear_on_submit=True):
        chat_col1, chat_col2 = st.columns([5, 1], gap="small")
        with chat_col1:
            user_input = st.text_input("Your question", placeholder="What were the main decisions made?", label_visibility="collapsed")
        with chat_col2:
            send_btn = st.form_submit_button("Send →", use_container_width=True)

    if send_btn and user_input.strip():
        with st.spinner("Thinking…"):
            answer = ask_question(r["rag_chain"], user_input.strip())
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

else:
    st.markdown("""
    <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5rem 2rem;text-align:center">
        <div style="font-size:4rem;margin-bottom:1rem">📝</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--text);margin-bottom:0.5rem">
            Ready to Analyze
        </div>
        <div style="color:var(--text-muted);font-size:0.85rem;max-width:380px;line-height:1.7">
            Upload a .mp3, .mp4, or .wav audio or video file in the sidebar. Choose your language, and hit <strong>Analyze Media</strong> to get started.
        </div>
        <div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
            <span class="badge badge-purple">Transcription</span>
            <span class="badge badge-cyan">Summarisation</span>
            <span class="badge badge-green">RAG Chat</span>
        </div>
    </div>""", unsafe_allow_html=True)