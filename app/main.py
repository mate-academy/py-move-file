import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    command, source_path, destination_path = command_split
    if command != "mv":
        return
    dir_name, file_to_copy = os.path.split(destination_path)
    if len(dir_name) > 0:
        os.makedirs(dir_name, exist_ok=True)
    with (
        open(source_path, "r") as source,
        open(destination_path, "w") as destination
    ):
        destination.write(source.read())
    os.remove(source_path)
