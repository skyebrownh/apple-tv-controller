import inquirer

from const import MenuAction

def get_menu_selection(num_devices: int):
    choices = MenuAction().get_actions()

    questions = [
        inquirer.List("action", message="Action", choices=choices),
        inquirer.List(
            "device_num", 
            message="Device Number", 
            choices=[num for num in range(1, num_devices + 1)], 
            ignore=lambda a: a["action"] == MenuAction.EXIT
        )
    ]

    answers = inquirer.prompt(questions)
    return (answers["device_num"] if answers["device_num"] else None, answers["action"])