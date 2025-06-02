import asyncio
from pyatv import scan, pair
from pyatv.const import Protocol

loop = asyncio.get_event_loop()

async def atv_controller():
    # scan for devices
    atvs = await scan(loop)
    for index, atv in enumerate(atvs):
        print(f"{index} Name: {atv.name}, Address: {atv.address}")
        for service in atv.services:
            print(f"{service}")
        print("\n")

    # pair from device selection
    apple_tv = int(input("Which apple tv do you want to pair (index): "))
    
    pairing = await pair(atvs[apple_tv], Protocol.AirPlay, loop)
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

async def main():
    await atv_controller()

if __name__ == '__main__':
    loop.run_until_complete(main())