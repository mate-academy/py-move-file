import os


def move_file(command: str) -> None:
    command, origin, copy = command.split()
    if command != "mv":
        print("Wrong command")
        return
    try:
        destination_path = os.path.dirname(copy)
        if destination_path:
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
        os.rename(origin, copy)
    except FileNotFoundError:
        print("There is no file with this name")
