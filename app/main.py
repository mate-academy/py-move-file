import os


def move_file(command: str) -> None:
    short_command, source, path = command.split()
    if short_command != "mv":
        return
    if "/" not in path:
        os.rename(source, path)
        return
    destination_directory = os.path.dirname(path)
    os.makedirs(destination_directory, exist_ok=True)
    with open(path, "w") as new_file, open(source, "r") as source_file:
        new_file.write(source_file.read())
    os.remove(source)
