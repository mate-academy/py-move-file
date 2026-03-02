import os


def move_file(command: str) -> None:
    parts_cmd = command.split(" ")
    if len(parts_cmd) != 3:
        return
    cmd, source, destination = parts_cmd
    if cmd != "mv":
        return

    if os.path.isdir(destination) or destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination_path = os.path.join(destination, os.path.basename(source))
    else:
        parts = destination.split("/")
        if len(parts) > 1:
            directory = os.path.join(*parts[:-1])
            os.makedirs(directory, exist_ok=True)
        destination_path = destination
    os.rename(source, destination_path)
