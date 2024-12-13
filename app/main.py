import os


class IncorrectCommand(Exception):
    """Error if command is not move"""


def move_file(command: str) -> None:
    command, copied_file, new_file = command.split()
    if command != "mv":
        raise IncorrectCommand("Function supports only mv command")

    if "/" in new_file:
        folders = os.path.split(new_file)[0]
        os.makedirs(folders, exist_ok=True)

    with open(copied_file, "r") as old_file, open(new_file, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(copied_file)
