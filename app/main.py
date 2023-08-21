import os


def move_file(command: str) -> None | str:
    command, source_file, location = command.split()
    path, moved_file = os.path.split(location)
    if command != "mv":
        return "Command is incorrect"
    if path:
        os.makedirs(path, exist_ok=True)
    os.rename(source_file, location)
