from os import mkdir, remove
from os.path import basename, dirname, join


def move_file(command: str) -> None:
    result = command.split(" ")
    if len(result) != 3 or result[0] != "mv":
        return
    source_file, destination_file = result[1:]

    if destination_file.endswith("/"):
        destination_file = join(destination_file, basename(source_file))

    directory = dirname(destination_file)

    if directory:
        current_directory = ""

        for part in directory.split("/"):
            current_directory = join(current_directory, part)

            try:
                mkdir(current_directory)
            except FileExistsError:
                pass

    with open(source_file, "r") as source:
        content = source.read()

    with open(destination_file, "w") as destination:
        destination.write(content)

    remove(source_file)
