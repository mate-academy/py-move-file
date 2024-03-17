import os


def move_file(command: str) -> None:
    command = command.split(" ")
    if len(command) != 3 or command[0] != "mv":
        raise ValueError("Use: mv <source_file> <new_file>")

    _, source_file, destination_file = command
    destination_path = os.path.dirname(destination_file)
    if not destination_path:
        os.rename(source_file, destination_file)
    else:
        os.makedirs(destination_path, exist_ok=True)
        os.replace(source_file, destination_file)
