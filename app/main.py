import os


def check_command_params(command: str,
                         old_file_name: str, path: str
                         ) -> bool:
    return True if (command == "mv"
                    and old_file_name.count(".") == 1
                    and path.count(".") == 1
                    and old_file_name != path) else False


def make_dir_on_path(path: str) -> None:
    path_split = os.path.split(path)[0]
    if path_split:
        os.makedirs(path_split, exist_ok=True)


def move_file(command: str) -> None:
    split = command.split()
    if len(split) == 3:
        command_name, file, path = split
        if check_command_params(command_name, file, path):
            make_dir_on_path(path)
            with open(file) as content, open(path, "w") as copy:
                copy.write(content.read())
            os.remove(file)
