import time
import asyncio
from transcript import transcript_async

key = ""
audio_uri = "https://ftsa.blob.core.windows.net/audio/english_15mins.wav"
locale = "en-US"
definition = {
    "inputLocales": [locale],
    "wordLevelTimestampsEnabled": True,
    "profanityFilterMode": "Masked",
    "channel": [0, 1]
}
start_time = time.time()

async def call_transcript_async():
    return await transcript_async(audio_uri, definition, key)

#response = transcript_async(audio_uri, definition, key)
loop = asyncio.get_event_loop()  
result = loop.run_until_complete(call_transcript_async())  

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: {} secs".format(elapsed_time))
print("Result: {}".format(result))