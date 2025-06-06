from pydantic import BaseModel
from models.enum import Action

class ConnectionRequest(BaseModel):
    device_name: str

class ActionRequest(BaseModel):
    device_name: str
    action: Action