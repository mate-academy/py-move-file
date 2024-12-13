from os import makedirs, path, replace


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, old_file_name, new_file_name = command.split()
        if command_name == "mv":
            directory_path = path.dirname(new_file_name)
            if directory_path:
                makedirs(directory_path, exist_ok=True)
                replace(old_file_name, new_file_name)
            else:
                replace(old_file_name, new_file_name)
