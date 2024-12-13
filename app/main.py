import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "mv":
        source_file = command_parts[1]
        new_file = command_parts[2]
        path, filename = os.path.split(new_file)
        if path:
            os.makedirs(path, exist_ok=True)
        os.replace(source_file, new_file)
        if os.path.exists(source_file):
            os.remove(source_file)
