from const import MenuAction
from core.menu import get_menu_selection

class AppleTVMenuController:
    def __init__(self, device):
        self.device = device

    async def run(self):
        while True:
            action = get_menu_selection()
            if action == MenuAction.EXIT:
                break
            await self.device.perform_action(action)