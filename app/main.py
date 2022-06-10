import os


def move_file(command):
    if "/" in command:
        ls = command.replace(" ", "/").split("/")
        origin_file_name = ls[1]
        moved_file_name = ls[-1]
        directories = ls[2:-1]
        path_name = ""
        for directory in directories:
            os.mkdir(f"{path_name}{directory}")
            path_name += directory + "/"
        with open(origin_file_name, "r") as origin_file,\
             open(f"{path_name}{moved_file_name}", "w") as created_file:
            text_to_copy = origin_file.read()
            created_file.write(text_to_copy)
        os.remove(origin_file_name)
