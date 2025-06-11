import asyncio

from pyatv import scan, pair, connect
from pyatv.const import Protocol

from models.enum import Action

class AppleTVDevice:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage
        self.device = None
        self.remote = None
    
    async def connect(self, loop):
        atvs = await scan(loop, protocol=Protocol.AirPlay, storage=self.storage)
        selected = next((d for d in atvs if d.name == self.name), None)
        
        # if not selected:
        #     print(f'Device "{self.name}" not found.')
        #     print(f'Finding other devices to pair...')
        #     selected = await pair_another_device(atvs, self.storage)

        self.device = await connect(selected, loop, self.storage)
        self.remote = self.device.remote_control

        # # sub function: pair_another_device
        # async def pair_another_device(atvs, storage):

        #     # loop through devices
        #     for index, atv in enumerate(atvs):
        #         print(f"{index} Name: {atv.name}, Address: {atv.address}")
        #         for service in atv.services:
        #             print(f"{service}")
        #         print("\n")

        #     # pair from device selection
        #     atv_input = int(input("Which apple tv do you want to pair (index): "))
        
        #     pairing = await pair(atvs[atv_input], Protocol.AirPlay, loop, storage=storage)
        #     await pairing.begin()

        #     pin = int(input("Pin: "))
        #     pairing.pin(pin)
        #     await pairing.finish()

        #     # give feedback on the process
        #     if pairing.has_paired:
        #         print("Paired with device!")
        #         print("Credentials: ", pairing.service.credentials)
        #     else:
        #         print("Did not pair with device")

        #     await pairing.close()
        #     return atvs[atv_input]
        
    async def disconnect(self):
        if self.device:
          await asyncio.gather(*self.device.close())
    
    async def perform_action(self, action):
        match action:
            case Action.UP:
                await self.remote.up() 
            case Action.DOWN:
                await self.remote.down()
            case Action.LEFT:
                await self.remote.left()
            case Action.RIGHT:
                await self.remote.right()
            case Action.SELECT:
                await self.remote.select()
            case Action.HOME:
                await self.remote.home()
            case Action.PREVIOUS:
                await self.remote.menu()
            case Action.PLAY_PAUSE:
                await self.remote.play_pause()
            case Action.SLEEP:
                await self.device.power.turn_off()    
            case _:
                pass
