import os


def move_file(command: str):
    command_name, file1, path = command.split(" ")
    path_list = path.split("/")
    path_len = len(path_list)
    parent_dir = ""
    for i, name in enumerate(path_list):
        if i < path_len - 1:
            parent_dir = os.path.join(parent_dir, name)
            os.mkdir(parent_dir)
    with open(file1, "r") as file_in, open(path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file1)
