import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_name, mv_file = command.split()
        path_folder_file = mv_file[0:mv_file.rfind("/") + 1]

        if command_name == "mv":

            if mv_file.count("/") > 0:

                os.makedirs(path_folder_file, exist_ok=True)

            os.rename(file_name, mv_file)
