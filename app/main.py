import os


def move_file(command):
    list_ = command.split(" ")
    file_first_name = list_[1]
    file_second_pathname = list_[2]
    if "/" in list_[2]:
        list_dir = list_[2].split("/")
        path = ""
        for dir_path in list_dir[:-1]:
            path += dir_path
            os.mkdir(path)
            path += "/"
    with open(file_first_name, "r") as first, \
            open(file_second_pathname, "w") as second:
        context = first.read()
        second.write(context)
    os.remove(file_first_name)
