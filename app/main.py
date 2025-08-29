import os
import shutil
from pathlib import Path


def move_file(command: str) -> None:
    command = command.strip().split(" ")
    if (command[0] == "mv"):
        file_origin = Path(str(command[1]))
        if file_origin.is_file():
            name_dir_2 = os.path.dirname(command[2])
            parts_dir_2 = Path(name_dir_2).parts
            atual = ""
            for path in parts_dir_2:
                atual = os.path.join(atual, path)
                if not os.path.exists(atual):
                    os.mkdir(atual)

            shutil.move(command[1], command[2])
