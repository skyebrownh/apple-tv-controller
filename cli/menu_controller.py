from cli.const import MenuAction
from cli.menu import get_menu_selection

class AppleTVMenuController:
    def __init__(self, devices):
        self.devices = devices

    async def run(self):
        while True:
            device_num, action = get_menu_selection(len(self.devices))
            if action == MenuAction.EXIT:
                break
            await self.devices[device_num - 1].perform_action(action)