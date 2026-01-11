import os


def move_file(command: str) -> None:
    command, origin, copy = command.split()
    if command == "mv" and os.path.isfile(origin):
        destination_path = os.path.dirname(copy)
        if destination_path:
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
        os.rename(origin, copy)
