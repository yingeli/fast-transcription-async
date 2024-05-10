import time
#import asyncio
from transcript import transcript

key = "275321276dcd4e438c734cdddb5e5985"
audio_uri = "https://oppobatchasrblobstorage.blob.core.windows.net/audios/en/english_30mins.wav?sp=r&st=2024-04-24T04:09:39Z&se=2024-12-31T12:09:39Z&spr=https&sv=2022-11-02&sr=b&sig=2RW0PzhJ3BGAqSuQvLQ%2Fz5NWrKhXOWwoOTd2TdkQiug%3D"
locale = "en-US"
definition = {
    "inputLocales": [locale],
    "wordLevelTimestampsEnabled": True,
    "profanityFilterMode": "Masked",
    "channel": [0, 1]
}
start_time = time.time()

response = transcript(audio_uri, definition, key)
#loop = asyncio.get_event_loop()  
#response = loop.run_until_complete(transcript_async(audio_uri, definition, key))  

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: {} secs".format(elapsed_time))

response.raise_for_status()
print("Response: {}".format(response))

json = response.json()

print("Response json: {}".format(json))