from os import path, replace, makedirs


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " mv <source_file> <destination_path>")

    mv_value, source_file, test_path = parts
    if mv_value == "mv":
        directory = path.dirname(test_path)
        if directory and not path.exists(directory):
            makedirs(path.dirname(test_path), exist_ok=True)
    else:
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " mv <source_file> <destination_path>")
    replace(source_file, test_path)
