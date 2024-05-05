# fast-transcription-async

Request 1:
curl -v -X POST -H "Ocp-Apim-Subscription-Key: xxxxxxxxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json" -d '{
    "config": {
        "inputLocales": ["en-US"],
        "wordLevelTimestampsEnabled": true,
        "profanityFilterMode": "Masked",
        "channel": [0, 1]
    },
    "audio": {
        "uri": "https://oppobatchasrblobstorage.blob.core.windows.net/audios/en/english_30mins.wav?sp=r&st=2024-04-24T04:09:39Z&se=2024-12-31T12:09:39Z&spr=https&sv=2022-11-02&sr=b&sig=2RW0PzhJ3BGAqSuQvLQ%2Fz5NWrKhXOWwoOTd2TdkQiug%3D"
    }
}' "https://ftsea.azurewebsites.net/speechtotext/v3.2_internal.1/asynctranscriptions"

Response JSON
{"name":"0fe1455a-a3f2-426f-ac0a-265f63aad52d"}

Request 2:
curl -v https://ftsea.azurewebsites.net/speechtotext/v3.2_internal.1/asynctranscriptions/0fe1455a-a3f2-426f-ac0a-265f63aad52d