from fastapi import FastAPI, Request
from bot import process_transaction_request  # if saved as bot.py

app = FastAPI()

@app.post("/process")
async def process(request: Request):
    data = await request.json()
    result = process_transaction_request(data)
    return result
