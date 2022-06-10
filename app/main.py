import os


def move_file(command: str):
    file_name, path_and_new_file_name = command.split()[1:]
    if "/" in path_and_new_file_name:
        new_file_name = path_and_new_file_name.split("/")[-1]
        path_to_new_file = path_and_new_file_name.split("/")[:-1]
        path_and_new_file_name = ""
        for dir in path_to_new_file:
            path_and_new_file_name += dir + "/"
            os.mkdir(path_and_new_file_name)
        path_and_new_file_name += new_file_name
    with open(file_name, "r") as file:
        source_file = file.read()
    with open(path_and_new_file_name, "w") as copy_file:
        copy_file.write(source_file)

    os.remove(file_name)
