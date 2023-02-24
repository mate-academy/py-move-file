import os
import shutil


def move_file(command: str) -> None:
    operation, file_in, file_to_move = command.split()
    if operation == "mv" and "/" not in file_to_move:
        os.rename(file_in, file_to_move)
    if operation == "mv" and "/" in file_to_move:
        path_generator = file_to_move.split("/")
        folder_index = 0
        path_for_creation = ""
        while folder_index < len(path_generator) - 1:
            path_for_creation += f"{path_generator[folder_index]}/"
            try:
                os.mkdir(path_for_creation)
            except FileExistsError:
                pass
            folder_index += 1
        shutil.move(file_in, f"{path_for_creation}{path_generator[-1]}")
