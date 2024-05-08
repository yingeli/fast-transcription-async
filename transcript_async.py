import os
import aiohttp

transcription_endpoint = os.environ.get("TRANSCRIPTION_ENDPOINT", "https://southeastasia.api.cognitive.microsoft.com/speechtotext/v3.2_internal.1/syncTranscriptions")

async def transcript_async(audio_uri, config, speech_service_key):
    async with aiohttp.ClientSession() as session:  
        async with session.get(audio_uri) as get_response:  
            get_response.raise_for_status()
   
            async with session.post(transcription_endpoint, data=get_response.content) as post_response:  
                # post_response.raise_for_status()
                return await post_response