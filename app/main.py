import os


def move_file(command: str):
    command_mv, current_file_name, new_file_name = command.split()

    if command_mv == "mv" and current_file_name != new_file_name:
        if os.path.isfile(new_file_name):
            return

        if new_file_name[-1] == os.path.sep:
            new_file_name += current_file_name

        full_path = ""
        for directory_name in new_file_name.split(os.path.sep)[:-1]:
            if not os.path.isdir(full_path + directory_name):
                os.mkdir(full_path + directory_name)
                full_path += directory_name + os.path.sep

        os.rename(current_file_name, new_file_name)
