from consolemenu import *
from consolemenu.items import *

from sys import argv
from uuid import uuid4
from shutil import copytree
from string import ascii_letters
from os import listdir, path, rename, system

system(f"echo '{argv[0]}' > /tmp/hfoiuhoiusdfhoiusdf.txt")

template_path = f"{path.dirname(argv[0])}/templates/"
projects_path = "/home/ganer/Projects/"
temp_projects_path = "/home/ganer/Projects/TEMP_PROJECTS/"
folder_name_replacement = "FOLDER_NAME"

make_uuid = lambda: ''.join(ascii_letters[i % len(ascii_letters)] for i in uuid4().bytes)

menu = ConsoleMenu("Choose a project template")

def replace_folder_names(loc, fold_name):
    for i in listdir(loc):
        if (spl := path.splitext(i))[0] == folder_name_replacement:
            rename(
                path.join(loc, i),
                path.join(loc, fold_name + spl[-1])
            )
    return loc

[
    menu.append_item(
        FunctionItem(i,
            lambda i = i: system(
                f"""cd {replace_folder_names(copytree(
                    path.join(template_path, i),
                    path.join(
                        projects_path if (
                            t := input(
                                'Enter project name (leave blank for temp project): '
                            ).strip()
                        ) else temp_projects_path,
                        (name := t if t else make_uuid())
                    )
                ), name)}; vscode ."""
            ) ^ exit()
        )
    ) for i in listdir(template_path)
]

menu.show()