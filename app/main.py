import os


def move_file(command: str) -> None:
    cmd, initial_file_path, copy_file_path = command.split()
    if "/" in copy_file_path:
        levels = copy_file_path.split("/")[0:-1]
        current_path = ""

        for level in levels:
            current_path = os.path.join(current_path, level)
            os.mkdir(current_path)
        open(copy_file_path[:-1], "x")
        os.remove(initial_file_path)

    else:
        os.rename(initial_file_path, copy_file_path)
