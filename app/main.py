from os import path, replace, makedirs


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " mv <source_file> <destination_path>")

    command_type, source_file, destination_path = parts
    if command_type != "mv":
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " mv <source_file> <destination_path>")

    if source_file == destination_path:
        raise ValueError("Source and destination paths cannot be the same.")

    destination_directory = path.dirname(destination_path)
    if destination_directory and not path.exists(destination_directory):
        makedirs(destination_directory, exist_ok=True)

    replace(source_file, destination_path)
