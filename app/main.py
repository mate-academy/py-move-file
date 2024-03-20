import os.path


def move_file(command: str) -> None:
    command_split = command.split(" ")
    if command_split[0] != "mv":
        return

    file_orig = command_split[1]
    file_new = command_split[2]

    if not os.path.dirname(file_new):
        os.replace(file_orig, file_new)
    else:
        path = os.path.dirname(file_new)
        os.makedirs(path, exist_ok=True)
        os.replace(file_orig, file_new)
