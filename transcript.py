import os
import requests
import json
import aiohttp
from azure.identity import DefaultAzureCredential

transcription_endpoint = os.environ.get("TRANSCRIPTION_ENDPOINT", "https://southeastasia.api.cognitive.microsoft.com/speechtotext/v3.2_internal.1/syncTranscriptions")

def get_access_token():
    token_credential = DefaultAzureCredential()  
    token_response = token_credential.get_token("https://storage.azure.com/")
    access_token = token_response.token
    return access_token

class HTTPError(Exception):  
    def __init__(self, status_code, reason, request_url):
        super().__init__(self)
        self.status_code = status_code
        self.reason = reason
        self.request_url = request_url      
    
    def __str__(self):
        error = {
            "status_code": self.status_code,
            "reason": self.reason,
            "request_url": self.request_url
        }
        return f"HTTP error: { json.dumps(error) }"

def transcript(audio_uri, config, speech_service_key):
    try:
        access_token = get_access_token()
        # headers = {"Authorization": f"Bearer {access_token}"}
        with requests.get(audio_uri, headers=headers, stream=True) as resp:  
            # ensure the request was successful  
            resp.raise_for_status()

            stream = resp.raw
            files = {
                'definition': (None, json.dumps(config), 'application/json'),
                'audio': ("audio", stream, 'application/octet-stream')
            }
            headers = {'Ocp-Apim-Subscription-Key': speech_service_key}
            with requests.post(transcription_endpoint, files=files, headers=headers) as response:
                response.raise_for_status()
                return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPError(e.response.status_code, e.response.reason, e.request.url)
        
async def transcript_async(audio_uri, config, speech_service_key):
    try:
        async with aiohttp.ClientSession() as session:
            access_token = get_access_token()
            #headers = {"Authorization": f"Bearer {access_token}"}
            async with session.get(audio_uri) as get_response:  
                get_response.raise_for_status()
                stream = get_response.content

                data = aiohttp.FormData()  
                data.add_field('definition', json.dumps(config), content_type='application/json')
                data.add_field('audio', stream, filename="audio", content_type='application/octet-stream') 

                headers = {'Ocp-Apim-Subscription-Key': speech_service_key}   
                async with session.post(transcription_endpoint, data=data, headers=headers) as post_response:
                    post_response.raise_for_status()
                    return await post_response.json()
    except aiohttp.ClientResponseError as e:
        raise HTTPError(e.status, e.message, str(e.request_info.url))