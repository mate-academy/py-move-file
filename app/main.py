import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        return

    source = command_list[1]
    destination = command_list[2]

    with open(source, "r") as f:
        content = f.read()

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory, filename = os.path.split(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(destination, "w") as f:
        f.write(content)

    os.remove(source)
