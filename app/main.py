import os


def move_file(command: str) -> None:
    file_name = command.split()
    if file_name[0] == "mv":
        if "/" in file_name[2]:
            os.makedirs(file_name[2])
        else:
            os.makedirs(file_name[1])
            os.rename(file_name[1], file_name[2])


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
