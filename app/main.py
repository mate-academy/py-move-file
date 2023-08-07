import os
from app.errors import check_for_errors, WrongCommand, NoSourceFile


def move_file(command: str) -> None:
    try:
        check_for_errors(command)

    except (WrongCommand, NoSourceFile) as e:
        print(e)
        return e

    command_name, filename, move_filename = command.split()

    current_dir = os.getcwd()
    source_path = os.path.join(current_dir, filename)
    destination_path = os.path.join(current_dir, move_filename)

    if "/" not in move_filename and "\\" not in move_filename:
        os.rename(source_path, destination_path)

    else:
        destination_dir = os.path.dirname(destination_path)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        with (
            open(source_path, "r") as file_in,
            open(destination_path, "a") as file_out
        ):
            for line in file_in:
                file_out.write(line)

        os.remove(source_path)
