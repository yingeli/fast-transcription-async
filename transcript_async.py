import os
import json
import aiohttp

transcription_endpoint = os.environ.get("TRANSCRIPTION_ENDPOINT", "https://southeastasia.api.cognitive.microsoft.com/speechtotext/v3.2_internal.1/syncTranscriptions")

async def transcript_async(audio_uri, config, speech_service_key):
    async with aiohttp.ClientSession() as session:  
        async with session.get(audio_uri) as get_response:  
            get_response.raise_for_status()
            stream = get_response.content

            data = aiohttp.FormData()  
            data.add_field('definition', json.dumps(config), content_type='application/json')
            data.add_field('audio', stream, filename="audio", content_type='application/octet-stream') 

            headers = {'Ocp-Apim-Subscription-Key': speech_service_key}   
            async with session.post(transcription_endpoint, data=data, headers=headers) as post_response:
                print("pre_raise_for_status")
                post_response.raise_for_status()
                print("pre_response")
                return await post_response.json()