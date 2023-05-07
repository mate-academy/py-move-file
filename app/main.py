import os


def move_file(command: str) -> str:
    command_split = command.split()
    mv_command, source_file, dir_and_file = command_split

    if mv_command != "mv":
        return "Input command is incorrect"
    if len(command_split) < 3:
        return "Error. One of the required values is missing"

    dir_line = dir_and_file.split("/")[:-1]
    new_file = dir_and_file.split("/")[-1]

    new_dir = ""
    if "/" in dir_and_file:
        for name in dir_line:
            new_dir = os.path.join(new_dir, name)
            try:
                os.mkdir(new_dir)
            except FileExistsError:
                pass
    os.rename(source_file, os.path.join(new_dir, new_file))

    return "File moved successfully."
