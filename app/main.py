from __future__ import annotations
import os


def move_clear_file(file_path1: str, file_path2: str) -> None:
    with (
        open(file_path1, "r") as file_in,
        open(file_path2, "w") as file_out
    ):
        file_out.write(file_in.read())
        file_in.close()
        os.remove(file_path1)


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("This is not valid")
    command, file_path_name1, file_path_name2 = command.split()
    if command != "mv":
        raise ValueError(
            f'"{command}" This is an invalid command!'
            f' The correct one is: "mv"'
        )

    path = os.path.join(file_path_name2)
    head_path, tail_path = os.path.split(path)

    if not head_path and tail_path:
        move_clear_file(file_path_name1, file_path_name2)

    if head_path and tail_path:
        current_path = ""
        for current_dir in head_path.split("/"):
            current_path = os.path.join(current_path, current_dir)
            if not os.path.isdir(current_path):
                os.mkdir(current_path)
        move_clear_file(file_path_name1, file_path_name2)
