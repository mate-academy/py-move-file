import os
from os.path import isdir


def move_file(command: str) -> None:
    command, source, destination = command.split()

    if command != "mv":
        return

    path_to_destination_dir = destination.split(os.sep)

    for dir_index in range(1, len(path_to_destination_dir)):
        if isdir(os.sep.join(path_to_destination_dir[:dir_index])):
            continue
        os.mkdir(os.sep.join(path_to_destination_dir[:dir_index]))

    with open(source) as s, open(destination, "w") as t:
        t.write(s.read())

    os.remove(source)
