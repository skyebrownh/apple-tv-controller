import asyncio
import inquirer

def main_menu():
    actions = [
        # "wake", 
        "up", 
        "down", 
        "left", 
        "right", 
        "select", 
        "home", 
        "previous", 
        "play/pause", 
        # "volume up", 
        # "volume down", 
        "sleep", 
        "exit"]

    question = [
        inquirer.List("action", message="Action", choices=actions)
    ]

    answer = inquirer.prompt(question)
    return answer["action"] if answer else None

async def handle_action(action, remote, device):
    match action:
        # case "wake":
            # FIXME: not working, need to find a workaround
            # await try_to_wake(device)
        case "up":
            await remote.up() 
        case "down":
            await remote.down()
        case "left":
            await remote.left()
        case "right":
            await remote.right()
        case "select":
            await remote.select()
        case "home":
            await remote.home()
        case "previous":
            await remote.menu()
        case "play/pause":
            await remote.play_pause()
        # case "volume up":
           # TODO: not working, need to find a workaround
           # await device.audio.volume_up() 
        # case "volume down":
            # TODO: not working, need to find a workaround
            # await device.audio.volume_down()
        case "sleep":
            await device.power.turn_off()    
        case _:
            pass

async def try_to_wake(device, retries=3, delay=3):
    for i in range(retries):
        try:
            await device.power.turn_on()
            await asyncio.sleep(1)
            await device.remote_control.home()
            print("Device should be awake now.")
            return
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            await asyncio.sleep(delay)
    print("Failed to wake Apple TV after multiple attempts.")