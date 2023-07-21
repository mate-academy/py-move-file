import os

from app.constants import (point, slash, short_command)


def check_command_params(split: list, command: str,
                         old_file_name: str, path: str
                         ) -> bool:
    if (len(split) == 3 and command == short_command
            and old_file_name.count(point) == 1 and path.count(point) == 1
            and old_file_name != path):
        return True
    return False


def make_dir_on_path(path: str) -> None:
    if path.count(slash) > 0:
        dir_level = ""
        for level in path.split(slash)[:-1]:
            dir_level += level + slash
            if not os.path.exists(dir_level):
                os.mkdir(dir_level)


def move_file(command: str) -> None:
    command_name, file, path = command.split()
    if check_command_params(command.split(), command_name, file, path):
        make_dir_on_path(path)
        with open(file) as content, open(path, "w") as copy:
            copy.write(content.read())
        os.remove(file)
