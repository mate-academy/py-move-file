import os


def check_command_params(command: str,
                         old_file_name: str, path: str
                         ) -> bool:
    if (command == "mv" and old_file_name.count(".") == 1
            and path.count(".") == 1
            and old_file_name != path):
        return True
    return False


def make_dir_on_path(path: str) -> None:
    if path.count("/") > 0:
        dir_path = "/".join(path.split("/")[:-1])
        os.makedirs(dir_path, exist_ok=True)


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file, path = command.split()
        if check_command_params(command_name, file, path):
            make_dir_on_path(path)
            with open(file) as content, open(path, "w") as copy:
                copy.write(content.read())
            os.remove(file)
