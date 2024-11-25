import os
from pathlib import Path


def move_file(command: str):
    files_name = command.split(" ")
    dir_and_file = []
    if "/" in files_name[2]:
        dir_and_file = files_name[2].split("/")
    else:
        dir_and_file.append(files_name[2])

    if files_name[1] == dir_and_file[-1]:
        return

    if len(command) > 1 and command.startswith("mv"):
        file_path = Path(files_name[2])
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with (open(files_name[1], "r") as file_in,
              open(file_path, "w") as file_out):
            file_out.writelines(file_in)
        os.remove(files_name[1])
    else:
        return
