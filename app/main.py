import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if split_command[0] != "mv" or len(split_command) != 3:
        return

    file_in = split_command[1]
    file_out = split_command[2]

    if not os.path.exists(file_in):
        return

    directories = os.path.dirname(file_out)

    if directories:
        os.makedirs(directories, exist_ok=True)

    os.replace(file_in, file_out)
