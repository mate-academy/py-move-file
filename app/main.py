import os


def move_file(command: str) -> None:
    split_command = command.split()
    elements = None
    if "/" in split_command[2]:
        elements = split_command[2].split("/")
    path = ""
    for element in elements:
        if "." not in element:
            path += element + "/"
            os.mkdir(path)
