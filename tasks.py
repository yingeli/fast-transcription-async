import os

from celery import Celery
from transcript import transcript

broker = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379")
transcriptions = Celery(__name__, broker=broker, backend=backend)

@transcriptions.task(name="transcript")
def run_transcript(audio_uri, definition, key):
    response = transcript(audio_uri, definition, key)
    response.raise_for_status()
    result = response.json()
    return result