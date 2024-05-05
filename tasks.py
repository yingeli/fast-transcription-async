import os
import requests
import json

from celery import Celery
from transcript import transcript

broker = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379")
transcriptions = Celery(__name__, broker=broker, backend=backend)

class JsonHTTPError(Exception):  
    def __init__(self, error):  
        super().__init__(error)  
        self.http_error = error
    
    def __str__(self):  
        return f"HTTP error: {self.http_error}"
    
@transcriptions.task(name="transcript")
def run_transcript(audio_uri, definition, key):
    try:
        response = transcript(audio_uri, definition, key)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error = {  
            'status_code': e.response.status_code,  
            'message': e.args[0]  
        }
        raise JsonHTTPError(json.dumps(error))