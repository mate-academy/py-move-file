import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError(
            "Command must have format: mv <source> <destination>"
        )

    _, source, destination = command_parts

    directories, _, filename = destination.rpartition("/")

    if not filename:
        filename = os.path.basename(source)

    if directories:
        current_path = ""
        for directory in directories.split("/"):
            current_path = os.path.join(current_path, directory)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    destination_path = os.path.join(directories, filename)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
