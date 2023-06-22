import os


def move_file(command: str) -> None:
    command_name, file_name, path_to_new_file = command.split()
    if command_name == "mv" and os.path.isfile(file_name):
        new_file = os.path.dirname(path_to_new_file)
        if new_file:
            if not os.path.exists(new_file):
                os.makedirs(new_file)
        os.rename(file_name, path_to_new_file)
