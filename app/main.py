import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise ValueError("Incorrect command input")
    source_file, destination_path = command[1], command[2]
    new_path = os.path.dirname(destination_path)
    if new_path:
        os.makedirs(new_path, exist_ok=True)
    os.replace(source_file, destination_path)
