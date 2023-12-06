import os


def create_valid_path(path: str) -> str | None:
    file_name = os.path.basename(path)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, file_name)


def move_file(command: str) -> None:
    command_elements = command.split()
    if len(command_elements) == 3:
        command, source_file, destination_path = command_elements
        if command == "mv":
            new_file = create_valid_path(destination_path)
            os.rename(source_file, new_file)
        if os.path.exists(source_file):
            os.remove(source_file)
