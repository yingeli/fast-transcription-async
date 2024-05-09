import time
import asyncio
from transcript import transcript_blob

key = ""
audio_uri = "https://oppobatchasrblobstorage.blob.core.windows.net/audios/en/english_30mins.wav?sp=r&st=2024-04-24T04:09:39Z&se=2024-12-31T12:09:39Z&spr=https&sv=2022-11-02&sr=b&sig=2RW0PzhJ3BGAqSuQvLQ%2Fz5NWrKhXOWwoOTd2TdkQiug%3D"
locale = "en-US"
definition = {
    "inputLocales": [locale],
    "wordLevelTimestampsEnabled": True,
    "profanityFilterMode": "Masked",
    "channel": [0, 1]
}
start_time = time.time()

async def call_transcript_async():
    return await transcript_blob(audio_uri, definition, key)

#response = transcript_async(audio_uri, definition, key)
loop = asyncio.get_event_loop()  
result = loop.run_until_complete(call_transcript_async())  

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: {} secs".format(elapsed_time))
print("Result: {}".format(result))