import asyncio

from core.storage import load_storage
from core.apple_tv_device import AppleTVDevice
from core.menu_controller import AppleTVMenuController

LOOP = asyncio.get_event_loop()

async def main():
    storage = await load_storage(LOOP)

    device = AppleTVDevice('Apt Alternate ATV', storage)
    await device.connect(LOOP)

    controller = AppleTVMenuController(device)
    await controller.run()

    await device.disconnect()

if __name__ == '__main__':
    LOOP.run_until_complete(main())