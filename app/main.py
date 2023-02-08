import os
from pathlib import Path


def move_file(command: str) -> None:
    splitted_all = command.split("/")
    splitted_first_str = str(splitted_all[0]).split()
    if len(splitted_all) == 1:
        if len(splitted_first_str) <= 2 or len(splitted_first_str) > 3:
            raise ValueError("no 'cp' command present or command syntax error")
        with open(splitted_first_str[1], "r") as source_f, \
                open(splitted_first_str[2], "w") as target_f:
            for line in source_f:
                target_f.write(line)
            os.remove(splitted_first_str[1])
    if len(splitted_all) >= 2:
        filename_2 = splitted_all[-1]
        path = "/".join([splitted_first_str[2]] + splitted_all[1:-1])
        dir_path = Path(path)
        target_file = dir_path / filename_2
        os.makedirs(path)
        with open(target_file, "w") as target_f,\
                open(splitted_first_str[1], "r") as source_f:
            for line in source_f:
                target_f.write(line)
            os.remove(splitted_first_str[1])
