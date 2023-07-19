import os


def move_file(command: str) -> None:
    splitted_cmd = command.split()
    if len(splitted_cmd) != 3:
        return
    if splitted_cmd[0] != "mv":
        return
    cmd, file_from, file_to = splitted_cmd
    if "/" in file_to or r"\\" in file_to:
        directory = os.path.dirname(file_to)
        os.makedirs(directory, exist_ok=True)
        with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
            file_to.write(file_from.read())
        os.remove(file_from.name)
    else:
        os.rename(file_from, file_to)
