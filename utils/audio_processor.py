import os
import tempfile
from pathlib import Path

import yt_dlp
from pydub import AudioSegment

DOWNLOAD_DIR = "downloades"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


# -------------------------------------------------------------------
# YouTube Download (Optional)
# -------------------------------------------------------------------
def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "retries": 10,
        "fragment_retries": 10,
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                " AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/137.0.0.0 Safari/537.36"
            )
        },
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return os.path.splitext(filename)[0] + ".wav"

    except Exception as e:
        raise Exception(f"YouTube download failed: {e}")


# -------------------------------------------------------------------
# Save Uploaded File
# -------------------------------------------------------------------
def save_uploaded_file(uploaded_file):
    """
    Save Streamlit uploaded file to a temporary location.
    """

    suffix = Path(uploaded_file.name).suffix

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    )

    temp_file.write(uploaded_file.read())
    temp_file.close()

    return temp_file.name


# -------------------------------------------------------------------
# Convert Audio / Video to WAV
# -------------------------------------------------------------------
def convert_to_wav(input_path: str) -> str:

    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    audio = AudioSegment.from_file(input_path)

    audio = (
        audio
        .set_channels(1)
        .set_frame_rate(16000)
    )

    audio.export(output_path, format="wav")

    return output_path


# -------------------------------------------------------------------
# Chunk Audio
# -------------------------------------------------------------------
def chunk_audio(
    wav_path: str,
    chunk_minutes: int = 10
):

    audio = AudioSegment.from_wav(wav_path)

    chunk_ms = chunk_minutes * 60 * 1000

    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_ms)):

        chunk = audio[start:start + chunk_ms]

        chunk_path = f"{wav_path}_chunk_{i}.wav"

        chunk.export(chunk_path, format="wav")

        chunks.append(chunk_path)

    return chunks


# -------------------------------------------------------------------
# Process Uploaded File
# -------------------------------------------------------------------
def process_uploaded_file(uploaded_file):

    input_path = save_uploaded_file(uploaded_file)

    wav_path = convert_to_wav(input_path)

    print("Chunking audio...")

    chunks = chunk_audio(wav_path)

    print(f"{len(chunks)} chunk(s) created.")

    return chunks


# -------------------------------------------------------------------
# Process Input
# -------------------------------------------------------------------
def process_input(source):

    """
    Supports:
    1. Streamlit UploadedFile
    2. Local path
    3. YouTube URL (optional)
    """

    if hasattr(source, "read"):

        print("Uploaded file detected.")

        return process_uploaded_file(source)

    elif isinstance(source, str):

        if source.startswith("http://") or source.startswith("https://"):

            print("YouTube URL detected.")

            wav_path = download_youtube_audio(source)

        else:

            print("Local file detected.")

            wav_path = convert_to_wav(source)

        chunks = chunk_audio(wav_path)

        return chunks

    else:

        raise ValueError("Unsupported input type.")