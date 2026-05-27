import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    command, file_in, file_out = split_command

    if command != "mv" or len(split_command) != 3:
        return

    if not os.path.exists(file_in):
        return

    directories = os.path.dirname(file_out)

    if directories:
        os.makedirs(directories, exist_ok=True)

    with open(file_in, "r") as source_file, open(file_out, "w") as target_file:
        target_file.write(source_file.read())

    os.remove(file_in)
