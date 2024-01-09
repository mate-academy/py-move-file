from os import makedirs, path, replace


def move_file(command: str) -> None:
    command_name, old_file_name, new_file_name = command.split()
    if command_name == "mv":
        if "/" in new_file_name:
            directory_path = path.dirname(new_file_name)
            makedirs(directory_path, exist_ok=True)
            replace(old_file_name, new_file_name)
        else:
            replace(old_file_name, new_file_name)
