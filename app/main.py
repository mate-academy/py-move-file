import os


def move_file(command: str) -> None:
    command_name, file_name, file_name_out, *_ = command.split()

    if command_name != "mv" and file_name == file_name_out:
        return

    directory = os.path.dirname(file_name_out)
    if directory:
        os.makedirs(directory, exist_ok=True)

    os.rename(file_name, file_name_out)
