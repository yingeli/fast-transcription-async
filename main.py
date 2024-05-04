from typing import Annotated
#from celery.result import AsyncResult
from fastapi import Body, FastAPI, Header
from fastapi.responses import JSONResponse

from tasks import run_transcript, transcriptions

app = FastAPI()

@app.post("/speechtotext/v3.2_internal.1/asynctranscriptions", status_code=201)
def transcript_async(payload = Body(...), ocp_apim_subscription_key: Annotated[str | None, Header()] = None):
    print("ocp_apim_subscription_key: {}".format(ocp_apim_subscription_key))
    print("payload: {}".format(payload))
    config = payload["config"]
    audio_uri = payload["audio"]["uri"]
    task = run_transcript.delay(audio_uri, config, ocp_apim_subscription_key)
    return JSONResponse({"name": task.id})

@app.get("/speechtotext/v3.2_internal.1/asynctranscriptions/{task_id}")
def get_transcription_status(task_id):
    task_result = transcriptions.AsyncResult(task_id)
    response = {
        "name": task_id,
        "status": task_result.status,
        "result": task_result.result
    }
    return JSONResponse(response)