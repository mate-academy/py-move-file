import os


def move_file(command: str) -> None:
    command, source, destination = command.split()

    if command != "mv":
        return

    path_to_destination_dir, destination_file = os.path.split(destination)

    try:
        os.makedirs(path_to_destination_dir)
    except FileExistsError:
        pass

    with open(source) as source_file, open(destination, "w") as target_file:
        target_file.write(source_file.read())

    os.remove(source)
