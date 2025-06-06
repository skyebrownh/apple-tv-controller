import asyncio

from fastapi import FastAPI, HTTPException, status

from utils.storage import load_storage
from models.apple_tv_device import AppleTVDevice
from models.request import ConnectionRequest, ActionRequest

# dictionary to hold connected devices for use in multiple routes
connected_devices: dict[str, AppleTVDevice] = {}

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

    # print(connected_devices)

    return {"status": f"{request.device_name} connected"}

# attempts to perform an action on a connected Apple TV
@app.post("/perform")
async def perform_action(request: ActionRequest):
    # print(connected_devices)

    atv = connected_devices[request.device_name]

    await atv.perform_action(request.action)

    return {"status": f"{request.action} action performed on {request.device_name}"}

# disconnect a connected Apple TV
@app.post("/disconnect")
async def disconnect(request: ConnectionRequest):
    atv = connected_devices[request.device_name]
    await atv.disconnect()
    connected_devices.pop(request.device_name)

    return {"status": f"{request.device_name} successfully disconnected"}