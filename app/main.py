import shutil
import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) == 3 and command.startswith("mv "):
        _, first_file_name, path_to_second_file = commands
        (path_to_second_file,
            second_file_name) = os.path.split(path_to_second_file)

        if path_to_second_file == "":
            os.rename(first_file_name, second_file_name)
            return

        if not os.path.exists(path_to_second_file):
            os.makedirs(path_to_second_file)

        path_to_second_file = os.path.join(path_to_second_file,
                                           second_file_name)
        shutil.move(first_file_name, path_to_second_file)
