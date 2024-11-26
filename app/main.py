import os


def move_file(command: str) -> None:
    parts_command = command.split()
    if len(parts_command) != 3 or parts_command[0] != "mv":
        return
    cmd, file_from, file_to = parts_command
    directory, filename = os.path.split(file_to)
    if directory:
        os.makedirs(directory, exist_ok=True)
        with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
            file_to.write(file_from.read())
        os.remove(file_from.name)
    else:
        os.rename(file_from, file_to)
