import requests
import time

key = "275321276dcd4e438c734cdddb5e5985"
audio_uri = "https://oppobatchasrblobstorage.blob.core.windows.net/audios/en/english_30min.wav?sp=r&st=2024-04-24T04:09:39Z&se=2024-12-31T12:09:39Z&spr=https&sv=2022-11-02&sr=b&sig=2RW0PzhJ3BGAqSuQvLQ%2Fz5NWrKhXOWwoOTd2TdkQiug%3D"
#audio_uri = "https://ftsa.blob.core.windows.net/audio/english_15mins.wav"
locale = "en-US"
data = {
    "config": {
        "inputLocales": [locale],
        "wordLevelTimestampsEnabled": True,
        "profanityFilterMode": "Masked",
        "channel": [0, 1]
    },
    "audio": {
        "uri": audio_uri
    }
}
headers = {'Ocp-Apim-Subscription-Key': key}
#api_uri = "http://localhost:8000/speechtotext/v3.2_internal.1/asynctranscriptions"
api_uri = "https://ftsea.azurewebsites.net/speechtotext/v3.2_internal.1/asynctranscriptions"

start_time = time.time()

response = requests.post(api_uri, json=data, headers=headers)

print("Response: {}".format(response))
print("Response status_code: {}".format(response.status_code))
print("Response json: {}".format(response.json()))

# pull result from task_id
task_id = response.json()["name"]
print("task_id: {}".format(task_id))

#api_uri = "http://localhost:8000/speechtotext/v3.2_internal.1/asynctranscriptions/{}".format(task_id)
api_uri = "https://ftsea.azurewebsites.net/speechtotext/v3.2_internal.1/asynctranscriptions/{}".format(task_id)
while True:
    response = requests.get(api_uri)
    print("Response: {}".format(response))
    print("Response status_code: {}".format(response.status_code))
    print("Response json: {}".format(response.json()))        

    response_json = response.json()
    status = response_json['status']
    print("status: {}".format(status))
    if status == 'SUCCESS' or status == 'FAILURE':        
        break

    time.sleep(1)  # wait for 10 seconds before polling again

result = response_json['result']
print("Result: {}".format(result))

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: {} secs".format(elapsed_time))