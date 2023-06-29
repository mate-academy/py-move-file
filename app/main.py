import os


def move_file(command: str) -> None:
    parts_of_command = command.split()

    if parts_of_command[0] != "mv" or len(parts_of_command) != 3:
        raise ValueError("Wrong command!")

    source = parts_of_command[1]
    destination = parts_of_command[2]
    destination_path = os.path.dirname(destination)

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)
    os.replace(source, destination)
