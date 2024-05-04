import os
import time

from celery import Celery
from transcript import transcript

#celery = Celery("transcript")
#celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
#celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

broker = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379")
transcriptions = Celery(__name__, broker=broker, backend=backend)

@transcriptions.task(name="transcript")
def run_transcript(audio_uri, definition, key):
    response = transcript(audio_uri, definition, key)
    result = response.json()
    return result