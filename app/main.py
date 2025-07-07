import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        return
    splitted_command = command.split()
    if len(splitted_command) != 3:
        return
    source = splitted_command[1]
    destination = splitted_command[2]

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
