import os
from app.functions_for_processing import (
    create_path,
    processing_files
)


def move_file(command: str) -> None:
    file_to_move, new_directory = command[3:len(command)].split(" ")
    path_list = new_directory.split("/")
    if path_list[-1] == "":
        create_path(path_list)
        os.remove(f"{file_to_move}")
        return
    with open(f"{file_to_move}", "r") as source:
        if len(path_list) == 1:
            processing_files(
                f"{path_list[0]}",
                "w",
                file_to_move,
                source
            )
        if len(path_list) > 1:
            create_path(path_list)
            processing_files(
                f"{os.path.join(*path_list[:len(path_list)])}",
                "w",
                file_to_move,
                source
            )
