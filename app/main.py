import os
import shutil


def move_file(command: str) -> None:
    file_name = command.split()
    if file_name[0] == "mv":
        if "/" in file_name[2]:
            second_file_name = "/".join(file_name[2].split("/")[-1:])
            file_directory = file_name[2].replace(second_file_name, "")
            os.makedirs(file_directory)
            shutil.copy(file_name[1], file_name[2])
        else:
            os.makedirs(file_name[1])
            os.rename(file_name[1], file_name[2])


move_file("mv file.txt file2.txt")
