import asyncio
from typing import Union
import threading
from fastapi import FastAPI, WebSocket

app = FastAPI()

async def convo(name):
    num = 0
    while True:
        num += 1
        await asyncio.sleep(1)

def convo_bridge(name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(convo(name))
    loop.close()

threading.Thread(target=convo_bridge, name="convo", args=(1,)).start()

@app.get("/")
def read_root():
    return {"Hello": "Balls"}


@app.websocket("/stream")
async def stream_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, world!")
    await websocket.close()
        