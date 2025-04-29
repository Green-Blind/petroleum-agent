from fastapi import FastAPI
from tasks import ping
from web3 import Web3
from config import settings

app = FastAPI()
w3 = Web3(Web3.LegacyWebSocketProvider(settings.rpc_url))


@app.post("/test-ping/")
async def test_ping():
    ping.delay()
    return {"status": "queued"}

@app.get("/health/")
async def health_check():
    chain = w3.eth.chain_id
    balance = w3.eth.get_balance(settings.wallet_address)
    return {
        "chain_id": chain,
        "address": settings.wallet_address,
        "balance_wei": balance
    }