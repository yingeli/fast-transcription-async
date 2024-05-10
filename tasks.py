import os
import asyncio

from celery import Celery
from transcript import transcript, transcript_async

broker = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379")
transcriptions = Celery(__name__, broker=broker, backend=backend)
    
@transcriptions.task(name="transcript")
def run_transcript(audio_uri, definition, key):
    result = transcript(audio_uri, definition, key)
    return result
    
@transcriptions.task(name="transcript_async")
def run_transcript_async(audio_uri, definition, key):
    result = asyncio.run(transcript_async(audio_uri, definition, key))  
    return result