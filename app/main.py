import os


def move_file(command: str) -> None:
    linux_mv = command.split()[0]
    first_file_name = command.split()[1]
    directory_file = command.split()[2]
    if linux_mv == "mv":
        if "/" in directory_file:
            os.makedirs(directory_file)
        else:
            os.makedirs(first_file_name)
            os.rename(first_file_name, directory_file)
