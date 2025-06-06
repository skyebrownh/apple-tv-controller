import asyncio

from utils.storage import load_storage
from models.apple_tv_device import AppleTVDevice
from cli.menu_controller import AppleTVMenuController

async def main():
    loop = asyncio.get_running_loop()

    storage = await load_storage(loop)

    device1 = AppleTVDevice('Apt Apple TV', storage)
    await device1.connect(loop)

    device2 = AppleTVDevice('Apt Alternate ATV', storage)
    await device2.connect(loop)

    controller = AppleTVMenuController([device1, device2])
    await controller.run()

    await device1.disconnect()
    await device2.disconnect()

if __name__ == '__main__':
    asyncio.run(main())