import asyncio
from typing import Union
import threading
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Balls"}


@app.websocket("/stream")
async def stream_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, world!")
    await websocket.close()