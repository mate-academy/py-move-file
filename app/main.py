import os


def move_file(command: str) -> None:
    if not command.startswith("mv "):
        return
    splitted_command = command.split()
    if len(splitted_command) != 3:
        return

    source = splitted_command[1]
    destination = splitted_command[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    abs_source = os.path.abspath(source)
    if destination.endswith("/"):
        abs_destination = os.path.abspath(
            os.path.join(destination, os.path.basename(source)))
    else:
        abs_destination = os.path.abspath(destination)

    if abs_source == abs_destination:
        raise ValueError(
            "Source and destination paths are the same. "
            "Move operation aborted.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as source_file:
        with open(destination, "w") as destination_file:
            destination_file.write(source_file.read())

    os.remove(source)
