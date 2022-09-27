from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    command_parts = command.split()
    file_name = command_parts[1]
    if "/" in command:
        file_path, file_name = command.rsplit("/", 1)
        makedirs(file_path)
    else:
        new_file_name = command_parts[-1]
        rename(file_name, new_file_name)
        return
    with open(file_name, "r") as source, \
            open(path.join(file_path, file_name), "w") as destination:
        destination.write(source.read())
        remove(file_name)
