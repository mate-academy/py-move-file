import os


def move_file(command: str):
    command_list = command.split()
    last_sl_ind = command_list[2].rfind("/")
    path_first = command_list[1]
    full_new_path = command_list[2]
    path_to_file = command_list[2][:last_sl_ind]
    os.makedirs(path_to_file)
    os.replace(path_first, full_new_path)
