import os
import shutil


def create_file(file_name, new_file):
    original = rf'{os.getcwd()}\{file_name}'
    target = rf'{os.getcwd()}\{new_file}'
    shutil.copyfile(original, target)
    os.remove(file_name)


def move_file(command_line: str):
    command, file_name, new_file = command_line.replace("/", "\\").split()

    assert command == "mv", f"Command:{command} is not defined"

    if "/" not in command_line:
        create_file(file_name, new_file)
    else:
        *path_new_file, new_file_name = new_file.split("\\")
        path = os.getcwd()
        for directory in path_new_file:
            path = os.path.join(path, directory)
        os.makedirs(path)

        create_file(file_name, new_file)
