import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    if command_parts[0] != "mv":
        return

    _, source_file_name, destination_path = command_parts

    destination_directory = os.path.dirname(destination_path)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    os.rename(source_file_name, destination_path)
