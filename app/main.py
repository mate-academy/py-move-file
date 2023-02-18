import os


class IncorrectCommand(Exception):
    """Error if command is not move"""


def move_file(command: str) -> None:
    command, copied_file, new_file = command.split()
    if command != "mv":
        raise IncorrectCommand("Function supports only mv command")

    if "/" in new_file:
        folders = new_file.split("/")[:-1]
        file_path = [folders[0]]
        for i in range(1, len(folders)):
            file_path.append(f"{file_path[i - 1]}/{folders[i]}")
        for directory in file_path:
            if not os.path.exists(directory):
                os.mkdir(directory)

    with open(copied_file, "r") as old, open(new_file, "w") as new:
        new.write(old.read())

    os.remove(copied_file)
