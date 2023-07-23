import os


def check_command_params(command: str,
                         old_file_name: str, path: str
                         ) -> bool:
    if (command == "mv"
            and old_file_name.count(".") == 1
            and path.count(".") == 1
            and old_file_name != path):
        return True
    return False


def make_dir_on_path(path: str) -> None:
    slashes = ["/", "\\"]
    for index, slash in enumerate(slashes):
        if path.count(slash) > 0 and slashes[index - 1] not in path:
            dir_path = slash.join(path.split(slash)[:-1])
            os.makedirs(dir_path, exist_ok=True)


def move_file(command: str) -> None:
    split = command.split()
    if len(split) == 3:
        command_name, file, path = split
        if check_command_params(command_name, file, path):
            make_dir_on_path(path)
            with open(file) as content, open(path, "w") as copy:
                copy.write(content.read())
            os.remove(file)
