import os
from app.errors import check_for_errors, WrongCommand, NoSourceFile


def move_file(command: str) -> None:
    try:
        check_for_errors(command)

    except (WrongCommand, NoSourceFile) as e:
        print(e)
        return

    command_name, source_name, path_new_file = command.split()
    path, filename = os.path.split(path_new_file)

    if path:
        os.makedirs(path, exist_ok=True)

    with (
        open(source_name, "r") as file_in,
        open(path_new_file, "a") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(source_name)
