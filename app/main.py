import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        command_name, file_name, mv_file = command_list
        path_folder_file = os.path.split(mv_file)

        if command_name == "mv":

            if mv_file.count("/") > 0:

                os.makedirs(path_folder_file[0], exist_ok=True)

            os.rename(file_name, mv_file)
