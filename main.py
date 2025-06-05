import asyncio

from core.storage import load_storage
from core.apple_tv_device import AppleTVDevice
from core.menu_controller import AppleTVMenuController

async def main():
    loop = asyncio.get_running_loop()

    storage = await load_storage(loop)

    device = AppleTVDevice('Apt Alternate ATV', storage)
    await device.connect(loop)

    controller = AppleTVMenuController(device)
    await controller.run()

    await device.disconnect()

if __name__ == '__main__':
    asyncio.run(main())