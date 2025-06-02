import asyncio
from pyatv import scan

loop = asyncio.get_event_loop()

async def atv_controller():
    atvs = await scan(loop)
    for atv in atvs:
        print(f"Name: {atv.name}, Address: {atv.address}")

async def main():
    await atv_controller()

if __name__ == '__main__':
    loop.run_until_complete(main())