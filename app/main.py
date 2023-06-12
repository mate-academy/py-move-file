import shutil
import os


def move_file(command: str) -> any:
    commands = command.split(" ")

    if len(commands) == 3 and command.startswith("mv "):
        _, first_file_name, path_to_second_file = commands
        bare_path_to_second_file = os.path.dirname(path_to_second_file)
        second_file_name = path_to_second_file.split("/")[-1]

        try:
            if "/" not in path_to_second_file:
                os.rename(first_file_name, second_file_name)
                return
        except FileNotFoundError as e:
            return str(e)

        if not os.path.exists(bare_path_to_second_file):
            os.makedirs(bare_path_to_second_file)

        shutil.move(first_file_name, path_to_second_file)
