import asyncio

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from enum import Enum

from core.storage import load_storage
from core.apple_tv_device import AppleTVDevice

# class as Enum for available actions to perform
class Action(str, Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    SELECT = 'select'
    HOME = 'home'
    PREVIOUS = 'previous'
    PLAY_PAUSE = 'play/pause'
    SLEEP = 'sleep'
    EXIT = 'exit'

# classes for Apple TV related endpoints request body
class ConnectionRequest(BaseModel):
    device_name: str

class ActionRequest(BaseModel):
    device_name: str
    action: Action

# dictionary to hold connected devices for use in multiple routes
connected_devices = {}

# initialize FastAPI
app = FastAPI()

# root endpoint that returns our UI interface
@app.get("/")
def index():
    return "webpage"

# attempts to connect to an Apple TV
@app.post("/connect")
async def connect(request: ConnectionRequest):
    loop = asyncio.get_running_loop()

    storage = await load_storage(loop)

    atv = AppleTVDevice(request.device_name, storage)
    await atv.connect(loop)

    connected_devices[request.device_name] = atv

    if not atv.device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{request.device_name} not found.")

    return {"status": f"{request.device_name} connected"}