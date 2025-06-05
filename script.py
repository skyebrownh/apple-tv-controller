import asyncio

from core.storage import load_storage
from core.apple_tv_device import AppleTVDevice
from core.menu_controller import AppleTVMenuController

async def main():
    loop = asyncio.get_running_loop()

    storage = await load_storage(loop)

    device1 = AppleTVDevice('Apt Apple TV', storage)
    await device1.connect(loop)

    device2 = AppleTVDevice('Apt Alternate ATV', storage)
    await device2.connect(loop)

    controller = AppleTVMenuController([device1, device2])
    await controller.run()

    device1.disconnect()
    device2.disconnect()

if __name__ == '__main__':
    asyncio.run(main())