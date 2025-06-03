import asyncio

from pyatv import scan, pair, connect
from pyatv.const import Protocol
from pyatv.storage.file_storage import FileStorage

from menu import main_menu, handle_action

TARGET_NAME = "Apt Alternate ATV"
LOOP = asyncio.get_event_loop()

async def atv_controller():
    # load storage
    storage = FileStorage.default_storage(LOOP)
    await storage.load()

    # scan and match by name
    atvs = await scan(LOOP, protocol=Protocol.AirPlay, storage=storage)
    selected = next((d for d in atvs if d.name == TARGET_NAME), None)

    # if not found, scan and pair
    if not selected:
        print(f"Device '{TARGET_NAME}' not found.")
        print("Finding other devices to pair...")
        selected = await pair_another_device(atvs, storage)

    # connect to paired device
    device = await connect(selected, LOOP, storage=storage)

    # perform actions
    remote = device.remote_control
    
    while True:
        action = main_menu()
        if action == "exit":
            break
        await handle_action(action, remote, device)

    # close connection
    device.close()

async def pair_another_device(atvs, storage):
    # loop through devices
    for index, atv in enumerate(atvs):
        print(f"{index} Name: {atv.name}, Address: {atv.address}")
        for service in atv.services:
            print(f"{service}")
        print("\n")

    # pair from device selection
    atv_input = int(input("Which apple tv do you want to pair (index): "))
    
    pairing = await pair(atvs[atv_input], Protocol.AirPlay, LOOP, storage=storage)
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
    return atvs[atv_input]

async def main():
    await atv_controller()

if __name__ == '__main__':
    LOOP.run_until_complete(main())