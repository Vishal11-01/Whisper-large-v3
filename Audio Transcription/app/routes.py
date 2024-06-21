from fastapi import APIRouter, File, UploadFile
from app.models import TranscriptionResult
from app.utils import process_audio_file

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResult)
async def transcribe_audio(file: UploadFile = File(...)):
    result = await process_audio_file(file)
    return result
