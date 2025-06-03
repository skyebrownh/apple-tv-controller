# storage.py 
# 
# define and load storage

from asyncio import AbstractEventLoop
from pyatv.storage.file_storage import FileStorage

async def load_storage(LOOP: AbstractEventLoop) -> FileStorage:
    storage: FileStorage = FileStorage.default_storage(LOOP)
    await storage.load()
    return storage