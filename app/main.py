import os


def move_file(command: str) -> str:
    command_split = command.split()
    if len(command_split) < 3:
        return "Error. One of the required values is missing"

    mv_command, source_file, dir_and_file = command_split

    if mv_command != "mv":
        return "Input command is incorrect"

    dir_line = dir_and_file.split("/")[:-1]
    new_file = dir_and_file.split("/")[-1]

    new_dir = ""
    if "/" in dir_and_file:
        for name in dir_line:
            new_dir = os.path.join(new_dir, name)
            os.makedirs(new_dir, exist_ok=True)
    os.rename(source_file, os.path.join(new_dir, new_file))

    return "File moved successfully."
