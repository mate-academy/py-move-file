import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        raise ValueError(
            "Invalid command format. Expected: mv <source> <destination>"
        )

    cmd, source, destination = command_list

    if cmd != "mv":
        raise ValueError("Only 'mv' command is supported")

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(destination):
        raise FileExistsError(
            f"Destination file '{destination}' already exists"
        )

    os.rename(source, destination)
