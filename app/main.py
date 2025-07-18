import os
from shutil import copy


def move_file(command: str) -> None:
    starting_dir = os.getcwd()
    cmnd = command.split()
    if len(cmnd) < 3 or cmnd[1].endswith("/"):
        raise ValueError("Wrong format of the command. "
                         "It should be like "
                         "'mv file.txt some_dir/new_file.txt'")
    source, destination = cmnd[1], cmnd[2]
    if not os.path.isfile(source):
        raise ValueError("The source file doesn't exist!")
    dest_path, dest_file = os.path.split(destination)
    if dest_path:
        os.makedirs(dest_path, exist_ok=True)
    try:
        copy(source, destination)
    except Exception as e:
        print(e)
    os.chdir(starting_dir)
    os.system("rm -v !('main.py')")
    os.remove(source)


if __name__ == "__main__":
    pass
