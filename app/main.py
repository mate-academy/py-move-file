import os


def move_file(command: str) -> str:
    command_split = command.split()
    if len(command_split) < 3:
        return "Error. One of the required values is missing"

    mv_command, source_file, dir_and_file = command_split

    if mv_command != "mv":
        return "Input command is incorrect"

    dir_path, new_file = os.path.split(dir_and_file)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    os.rename(source_file, os.path.join(dir_path, new_file))

    return "File moved successfully."
