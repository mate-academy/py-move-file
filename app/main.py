from os import mkdir, path, remove
from shutil import copy


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv_command, file_in_name, file_out_path = command_list
        if mv_command == "mv" and file_in_name != file_out_path:
            if "/" in file_out_path:
                file_out_path_tuple = tuple(file_out_path.split("/"))
                for i in range(1, len(file_out_path_tuple)):
                    new_dir_path = path.join(*file_out_path_tuple[:i])
                    if not path.exists(new_dir_path):
                        mkdir(new_dir_path)
                file_out_path = path.join(*file_out_path_tuple)
            copy(file_in_name, file_out_path)
            remove(file_in_name)
