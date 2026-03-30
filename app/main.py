import os


def move_file(command: str) -> None:
    if "-" in command:
        return
    command_data = command.split()
    command_name, source, destination = command_data
    if "/" in destination:
        destination_path = os.path.dirname(destination)
        os.makedirs(destination_path, exist_ok=True)

    os.rename(source, destination)
