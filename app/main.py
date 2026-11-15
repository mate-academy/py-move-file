import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination += os.path.basename(source)

    directory = os.path.dirname(destination)

    if directory:
        current_path = ""

        for directory_name in directory.split("/"):
            current_path = os.path.join(current_path, directory_name)

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
