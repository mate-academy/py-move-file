import os
from os import rename

delimiter = "/"


def move_file(command: str) -> None:
    command_list = command.strip().split()

    if not is_valid_command(command_list):
        return

    _, file_in_name, file_out_name = command_list

    if delimiter not in file_out_name:
        rename(file_in_name, file_out_name)
        return

    try:
        with (open(file_in_name, "r") as file_in):
            create_dirs(file_out_name)

            with (open(file_out_name, "w") as file_out):
                file_out.write(file_in.read())

        os.remove(file_in_name)
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")


def is_valid_command(command_list: list[str]) -> bool:
    return len(command_list) == 3 and command_list[0] == "mv"


def rename_file(file_in_name: str, file_out_name: str) -> None:
    rename(file_in_name, file_out_name)


def create_dirs(file_out_name: str) -> None:
    dirs = file_out_name.split(delimiter)
    dirs.pop()
    path = ""

    for dir_el in dirs:
        path = path + dir_el + delimiter

        try:
            os.mkdir(path)
        except FileExistsError:
            print(f"Directory {path} already exists")
