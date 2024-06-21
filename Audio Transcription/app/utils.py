import os
import torch
from whisper import load_model as load_whisper
from transformers import pipeline
from app.models import TranscriptionResult

# Check if GPU is available and set device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Whisper model on GPU
whisper_model = load_whisper("large-v3", device=device)


summarizer = pipeline("summarization", device=0 if device == "cuda" else -1)

def extract_timestamps(transcription: str) -> list:
    
    return [(0, 10, "Event 1"), (11, 20, "Event 2")]  

async def process_audio_file(file):
    temp_file_path = f"data/temp/{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file.file.read())

    transcription_result = whisper_model.transcribe(temp_file_path)

    transcription_text = transcription_result["text"]

    summary_result = summarizer(transcription_text, max_length=150, min_length=30, do_sample=False)
    summary_text = summary_result[0]['summary_text']

    timestamps = extract_timestamps(transcription_text)

    os.remove(temp_file_path)

    return TranscriptionResult(transcription=transcription_text, summary=summary_text, timestamps=timestamps)
