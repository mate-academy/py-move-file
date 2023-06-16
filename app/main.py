from os import mkdir, path, remove
from shutil import copy


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv_command, file_in_name, file_out_path = command_list
        if mv_command == "mv" and file_in_name != file_out_path:
            if "/" in file_out_path:
                dir_path_list = file_out_path.split("/")[:-1]
                current_dir_path = ""
                for directory in dir_path_list:
                    current_dir_path += directory + "/"
                    if not path.exists(current_dir_path):
                        mkdir(current_dir_path)
            copy(file_in_name, file_out_path)
            remove(file_in_name)
