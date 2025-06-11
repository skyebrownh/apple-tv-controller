from pyatv.storage.file_storage import FileStorage

async def load_storage(loop) -> FileStorage:
    storage = FileStorage.default_storage(loop)
    await storage.load()
    return storage