from fastapi import FastAPI
from tasks import ping

app = FastAPI()
@app.post("/test-ping/")
async def test_ping():
    ping.delay()
    return {"status": "queued"}
