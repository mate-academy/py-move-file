import os


def move_file(command: str) -> None:
    command_parts = command.split()

    source = command_parts[1]
    destination = command_parts[2]

    if os.path.exists(source):
        destination_dir = os.path.dirname(destination)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

        os.rename(source, destination)
