import os


def move_file(command: str) -> None:
    command_name, file_name, mv_file = command.split()
    path_folder_file = mv_file[0:mv_file.rfind("/") + 1]

    if len(command.split()) == 3 and command_name == "mv":

        if mv_file.count("/") > 0:

            if not os.path.exists(path_folder_file):
                os.makedirs(path_folder_file)

        if not os.path.exists(mv_file):
            os.rename(file_name, mv_file)
