import asyncio
import logging

from fastapi import FastAPI, HTTPException, status

from utils.storage import load_storage
from models.apple_tv_device import AppleTVDevice
from models.request import ConnectionRequest, ActionRequest
from utils.exceptions import register_exception_handlers

logging.basicConfig(level=logging.INFO)

# dictionary to hold connected devices for use in multiple routes
connected_devices: dict[str, AppleTVDevice] = {}

# initialize FastAPI
app = FastAPI()

register_exception_handlers(app)

# root endpoint that returns our UI interface
@app.get("/")
def index():
    logging.info("Root (/) route called")
    return "webpage"

# attempts to connect to an Apple TV
@app.post("/connect")
async def connect(request: ConnectionRequest):
    logging.info("Connect route called")
    loop = asyncio.get_running_loop()

    storage = await load_storage(loop)
    logging.info("Storage loaded")

    atv = AppleTVDevice(request.device_name, storage)
    logging.info("Connecting to device...")
    await atv.connect(loop)

    connected_devices[request.device_name] = atv
    logging.info(f"Connected devices: {connected_devices}")

    if not atv.device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{request.device_name} not found.")

    logging.info(f"{request.device_name} connected")
    return {"status": f"{request.device_name} connected"}

# attempts to perform an action on a connected Apple TV
@app.post("/perform")
async def perform_action(request: ActionRequest):
    logging.info("Perform route called")

    atv = connected_devices[request.device_name]

    await atv.perform_action(request.action)

    logging.info(f"{request.action} action performed on {request.device_name}")
    return {"status": f"{request.action} action performed on {request.device_name}"}

# disconnect a connected Apple TV
@app.post("/disconnect")
async def disconnect(request: ConnectionRequest):
    logging.info("Disconnect route called")

    atv = connected_devices[request.device_name]
    await atv.disconnect()
    connected_devices.pop(request.device_name)

    logging.info(f"{request.device_name} successfully disconnected")
    logging.info(f"Connected devices: {connected_devices}")
    return {"status": f"{request.device_name} successfully disconnected"}