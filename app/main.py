import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        raise ValueError("Invalid command format")

    _, file, path = command_list

    if path.endswith("/"):
        os.makedirs(os.path.normpath(path), exist_ok=True)
        os.rename(file, f"{os.path.join(path + file)}")
    elif "/" not in path:
        os.rename(file, path)
    else:
        os.makedirs(os.path.normpath(os.path.dirname(path)), exist_ok=True)
        os.rename(file, path)
