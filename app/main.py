import os


def move_file(command: str) -> None:
    split_command = command.split()

    if split_command[0] != "mv":
        return

    source = split_command[1]
    destination = split_command[2]
    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(source, destination)
