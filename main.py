import asyncio
import logging

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from utils.storage import load_storage
from models.apple_tv_device import AppleTVDevice
from models.request import ConnectionRequest, ActionRequest
from utils.exceptions import register_exception_handlers

logging.basicConfig(level=logging.INFO)

# dictionary to hold connected devices for use in multiple routes
connected_devices: dict[str, AppleTVDevice] = {}

# initialize FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

register_exception_handlers(app)

# root endpoint that returns our UI interface
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    logging.info("Root (/) route called")
    return templates.TemplateResponse(request=request, name="index.html", context={ 
        "devices": [
            { "name": "Apt Apple TV", "short_name": "MAIN" },
            { "name": "Apt Alternate ATV", "short_name": "ALT" },
        ]
     })

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