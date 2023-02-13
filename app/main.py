import os
import shutil


def move_file(command: str) -> None:
    command_mv, file_to_opening, directory_to_writing = command.split(" ")
    if command_mv == "mv":
        if directory_to_writing.count("/"):

            directory_to_writing_in_list = directory_to_writing.split("/")
            file_to_writing = directory_to_writing_in_list[-1]
            folders = ""
            for ind in range(len(directory_to_writing_in_list) - 1):
                folders += directory_to_writing_in_list[ind]
                os.mkdir(folders)
                folders += "/"
            shutil.copyfile(file_to_opening, folders + file_to_writing)
            os.remove(file_to_opening)
        else:

            shutil.copyfile(file_to_opening, directory_to_writing)
            os.remove(file_to_opening)
