import inquirer

from const import MenuAction

def get_menu_selection():
    actions = MenuAction().get_actions() 

    question = [
        inquirer.List("action", message="Action", choices=actions)
    ]

    answer = inquirer.prompt(question)
    return answer["action"] if answer else None