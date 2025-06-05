from pyatv import scan, pair, connect
from pyatv.const import Protocol

from const import MenuAction

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

        if not selected:
            print(f"ATV DEVICE CONNECT ERROR: device {self.name} not found!")
            return

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
        
    def disconnect(self):
        if self.device:
            self.device.close()
    
    async def perform_action(self, action):
        match action:
            case MenuAction.UP:
                await self.remote.up() 
            case MenuAction.DOWN:
                await self.remote.down()
            case MenuAction.LEFT:
                await self.remote.left()
            case MenuAction.RIGHT:
                await self.remote.right()
            case MenuAction.SELECT:
                await self.remote.select()
            case MenuAction.HOME:
                await self.remote.home()
            case MenuAction.PREVIOUS:
                await self.remote.menu()
            case MenuAction.PLAY_PAUSE:
                await self.remote.play_pause()
            case MenuAction.SLEEP:
                await self.device.power.turn_off()    
            case _:
                pass
