import os
import shutil


def move_file(command: str) -> None:
    commands = command.split(" ")

    if any([
        len(commands) != 3,
        not command.startswith("mv"),
        command.endswith("/")
    ]):
        return None

    command, old_file, new_file = commands

    if new_file.find("/") == -1:
        os.rename(old_file, new_file)
        return None

    new_file_path_list = new_file.split("/")

    directory_path = os.getcwd()
    for directory in new_file_path_list[:-1]:
        directory_path = os.path.join(directory_path, directory)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    new_file_path = os.path.join(directory_path, new_file_path_list[-1])
    shutil.move(old_file, new_file_path)
