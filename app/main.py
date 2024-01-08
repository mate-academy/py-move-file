from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    command_name, old_file_name, new_file_name = command.split()
    if command_name == "mv" and "/" in new_file_name:
        directory_path = path.dirname(new_file_name)
        makedirs(directory_path, exist_ok=True)
        with (
            open(old_file_name, "r") as old_file,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(old_file.read())
        remove(old_file_name)
    else:
        rename(old_file_name, new_file_name)
