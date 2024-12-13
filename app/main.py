import os


def move_file(command: str) -> None:
    command, source_file, destination = command.split()

    if os.path.dirname(destination):
        target_directory = os.path.dirname(destination)

        os.makedirs(target_directory, exist_ok=True)

    os.replace(source_file, destination)
