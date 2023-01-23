import os


def move_file(command: str) -> None:
    try:
        input_command, current_file, copied_file_path = command.split()
    except ValueError:
        raise ValueError("Command is incorrect")
    if input_command != "mv" or not os.path.exists(current_file):
        raise ValueError("Command is incorrect")
    copied_file_info = copied_file_path.split("/")
    if len(copied_file_info) > 1:
        path = ("/".join(copied_file_info[:-1]))
        os.makedirs(path)
    os.rename(current_file, copied_file_path)
