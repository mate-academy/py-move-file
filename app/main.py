import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    operator, source, destination = command_list
    if operator != "mv":
        return
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    os.rename(source, destination)
