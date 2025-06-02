import asyncio
from pyatv import scan, pair, connect
from pyatv.const import Protocol
from pyatv.storage.file_storage import FileStorage

loop = asyncio.get_event_loop()

async def atv_controller():
    # storage
    storage = FileStorage.default_storage(loop)
    await storage.load()

    # scan for devices
    atvs = await scan(loop, protocol=Protocol.AirPlay, storage=storage)
    for index, atv in enumerate(atvs):
        print(f"{index} Name: {atv.name}, Address: {atv.address}")
        for service in atv.services:
            print(f"{service}")
        print("\n")

    # pair from device selection
    atv_input = int(input("Which apple tv do you want to pair (index): "))
    
    pairing = await pair(atvs[atv_input], Protocol.AirPlay, loop, storage=storage)
    await pairing.begin()

    pin = int(input("Pin: "))
    pairing.pin(pin)
    await pairing.finish()

    # give feedback on the process
    if pairing.has_paired:
        print("Paired with device!")
        print("Credentials: ", pairing.service.credentials)
    else:
        print("Did not pair with device")

    await pairing.close()

    # connect to paired device
    connect_atv = await connect(atvs[atv_input], loop, storage=storage)
    print(connect_atv.device_info)
    connect_atv.close() 

async def main():
    await atv_controller()

if __name__ == '__main__':
    loop.run_until_complete(main())