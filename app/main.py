import shutil
import os


def move_file(command: str) -> any:
    commands = command.split(" ")

    if len(commands) < 3:
        return "wrong quantity of commands"

    very_bed_name_for_variable_cmd = commands[0]
    first_file_name = commands[1]
    path_to_second_file = commands[2]
    bare_path_to_second_file = os.path.dirname(commands[2])
    second_file_name = commands[2].split("/")[-1]

    if very_bed_name_for_variable_cmd != "mv":
        return "there is nothing to do)"

    try:
        if "/" not in path_to_second_file:
            os.rename(first_file_name, second_file_name)
            return
    except FileNotFoundError as e:
        return e

    if not os.path.exists(bare_path_to_second_file):
        os.makedirs(bare_path_to_second_file)

    shutil.move(first_file_name, path_to_second_file)
