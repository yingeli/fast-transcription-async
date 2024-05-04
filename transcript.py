import os
import requests
import json

transcription_endpoint = os.environ.get("TRANSCRIPTION_ENDPOINT", "https://southeastasia.api.cognitive.microsoft.com/speechtotext/v3.2_internal.1/syncTranscriptions")

def transcript(audio_uri, config, speech_service_key):
    with requests.get(audio_uri, stream=True) as resp:  
        # ensure the request was successful  
        resp.raise_for_status()

        stream = resp.raw
        files = {
            'definition': (None, json.dumps(config), 'application/json'),
            'audio': ("audio", stream, 'application/octet-stream')
        }
        headers = {'Ocp-Apim-Subscription-Key': speech_service_key}
        with requests.post(transcription_endpoint, files=files, headers=headers) as response:
            # response.raise_for_status()
            return response