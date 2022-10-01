import os
import shutil


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and not command.endswith("/"):
        file_remove = command.split()[1]
        new_file = command.split()[2].split("/")[-1]
        file_path = command.split()[2].split("/")[:-1]
        cur_dir = os.getcwd()

        for directory in file_path:
            os.mkdir(directory)
            os.chdir(directory)
        new_dir = os.getcwd()

        shutil.move(src=f"{cur_dir}\\{file_remove}", dst=f"{new_dir}")
        os.rename(f"{new_dir}\\{file_remove}", f"{new_dir}\\{new_file}")
