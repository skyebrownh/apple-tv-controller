from pyatv.storage.file_storage import FileStorage

async def load_storage(LOOP) -> FileStorage:
    storage = FileStorage.default_storage(LOOP)
    await storage.load()
    return storage