import os
import shutil


def move_file(command: str) -> None:
    _, file, new_file = command.split()
    if file == new_file:
        return
    if "/" not in new_file:
        shutil.move(file, new_file)
        return
    end_path = new_file.split("/")
    directory = end_path[:-1]
    file_name = end_path[-1]
    path_for_directory = os.path.join(*directory)
    path_for_file = os.path.join(*directory, file_name)
    os.makedirs(path_for_directory, exist_ok=True)
    shutil.move(file, path_for_file)
