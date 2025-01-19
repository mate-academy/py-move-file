import os


def move_file(command: str) -> None:
    cmd_name, file, destination = command.split()

    if cmd_name == "mv" and len(command.split()) == 3:
        if destination.endswith("/"):
            os.makedirs(destination, exist_ok=True)
            os.rename(file, f"{destination}{file}")
        elif "/" not in destination:
            os.rename(file, destination)
        else:
            *dirs, new_file = destination.split("/")
            path = "/".join(dirs)
            os.makedirs(path, exist_ok=True)
            os.rename(file, destination)
