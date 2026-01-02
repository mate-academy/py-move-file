import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 and split_command[0] == "mv":
        raise ValueError("Invalid command")
    source_command, source_path, destination_path = split_command
    destination_directory = os.path.dirname(destination_path)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)
    os.replace(source_path, destination_path)
