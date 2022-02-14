from uuid import uuid4
from shutil import copytree
from consolemenu import *
from consolemenu.items import *
from os import listdir, path, system
from string import ascii_letters, digits

template_path = "/home/ganer/Projects/Project_Templater/templates/"
projects_path = "/home/ganer/Projects/"
temp_projects_path = "/home/ganer/Projects/TEMP_PROJECTS/"

characters = ascii_letters + digits
make_uuid = lambda: ''.join(characters[i % len(characters)] for i in uuid4().bytes)

menu = ConsoleMenu("Choose a project template")

[
    menu.append_item(
        FunctionItem(i,
            lambda i = i: system(
                f"""cd {copytree(
                    path.join(template_path, i),
                    path.join(
                        projects_path if (
                            t := input(
                                'Enter project name (leave blank for temp project)'
                            ).strip()
                        ) else temp_projects_path,
                        t if t else make_uuid()
                    )
                )}; vscode ."""
            ) ^ exit()
        )
    ) for i in listdir(template_path)
]

# menu_item = MenuItem("Menu Item")
# function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
# command_item = CommandItem("Run a console command",  "touch hello.txt")
# selection_menu = SelectionMenu(["item1", "item2", "item3"])
# submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

menu.show()