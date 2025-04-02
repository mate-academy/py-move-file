import os
import shutil


def move_file(command: str) -> None:
    command_str = command.split()

    if len(command_str) != 3 or command_str[0] != "mv":
        raise ValueError
    source, target = command_str[1], command_str[2]

    if not os.path.isfile(source):
        raise FileNotFoundError

    if target.endswith("/"):
        os.makedirs(target, exist_ok=True)
        target = os.path.join(target, os.path.basename(source))
    else:
        dir_path = os.path.dirname(target)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    shutil.move(source, target)
