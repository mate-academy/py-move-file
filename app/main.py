from __future__ import annotations
import os


def move_clear_file(source_file: str, target_file: str) -> None:
    with (
        open(source_file, "r") as file_in,
        open(target_file, "w") as file_out
    ):
        file_out.write(file_in.read())
        file_in.close()
        os.remove(source_file)


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("This is not valid")
    command, source_file, target_file = command.split()
    if command != "mv":
        raise ValueError(
            f'"{command}" This is an invalid command!'
            f' The correct one is: "mv"'
        )

    path = os.path.join(target_file)
    head_path, tail_path = os.path.split(path)

    if not head_path and tail_path:
        move_clear_file(source_file, target_file)

    if head_path and tail_path:
        current_path = ""
        for current_dir in head_path.split("/"):
            current_path = os.path.join(current_path, current_dir)
            if not os.path.isdir(current_path):
                os.mkdir(current_path)
        move_clear_file(source_file, target_file)
