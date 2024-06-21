from pydantic import BaseModel

class TranscriptionResult(BaseModel):
    transcription: str
    summary: str
    timestamps: list
