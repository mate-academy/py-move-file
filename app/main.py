from os import path, remove, makedirs, rename


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) == 3 and command_list[0] == "mv":
        action, source_file_name, new_file_name = command_list

        if path.dirname(new_file_name):
            makedirs(path.dirname(new_file_name), exist_ok=True)
            with (
                open(source_file_name) as source_file,
                open(new_file_name, "w") as new_file
            ):
                new_file.write(source_file.read())
            remove(source_file_name)
        else:
            rename(source_file_name, new_file_name)
