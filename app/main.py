import os


def move_file(command: str) -> None:
    command_line = command.split()
    if len(command_line) != 3 or command_line[0] != "mv":
        return

    _, file, path_to_file = command_line

    if os.path.exists(file):
        file_dir = os.path.dirname(path_to_file)
        if file_dir and not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        os.rename(file, path_to_file)
