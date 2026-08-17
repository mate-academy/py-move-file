from os import makedirs, remove
from os.path import basename, dirname


def move_file(command: str) -> None:
    result = command.split(" ")
    source_file = result[1]
    destination_file = result[2]

    if destination_file.endswith("/"):
        destination_file = destination_file + basename(source_file)

    directory = dirname(destination_file)

    if directory:
        makedirs(directory, exist_ok=True)

    with open(source_file, "r") as source:
        content = source.read()

    with open(destination_file, "w") as destination:
        destination.write(content)

    remove(source_file)
