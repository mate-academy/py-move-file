import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, source, destination = command_list

    with open(source, "r") as f:
        content = f.read()

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)

    if directory:
        directories = directory.split("/")

        current_path = ""

        for folder in directories:
            current_path = os.path.join(current_path, folder)

            if not os.path.isdir(current_path):
                os.mkdir(current_path)

    with open(destination, "w") as f:
        f.write(content)

    os.remove(source)
