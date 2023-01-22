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
        path = ""
        for folder_name in copied_file_info[:-1]:
            path = os.path.join(path, folder_name)
            os.mkdir(path)
    os.rename(current_file, copied_file_path)
