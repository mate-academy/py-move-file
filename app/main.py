import os


def move_file(command: str) -> None:
    ls_of_command = command.split()

    destination_dir = os.path.dirname(ls_of_command[-1])
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(ls_of_command[1], ls_of_command[-1])
