import os


def move_file(command: str) -> None:
    command_name, source, destination = command.split()

    if command_name != "mv" or len(command.split()) != 3:
        raise Exception("You entered the wrong command!")

    destination_path = os.path.dirname(destination)

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)

    os.replace(source, destination)
