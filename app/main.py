from os import makedirs, remove
from os.path import exists


def move_file(command: str) -> None:
    command = command.split(" ")
    source_file = command[1]
    new_file = command[2]
    new_file_path = "/".join(new_file.split("/")[:-1])

    if new_file_path and not exists(new_file_path):
        makedirs(new_file_path)

    with open(source_file, "r") as source, open(new_file, "w") as moved_file:
        moved_file.write(source.read())

    remove(source_file)
