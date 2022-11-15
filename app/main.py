import os


def move_file(command: str) -> None:
    command_mv, file_name, path_new_file = command.split(" ")
    count_of_dir = path_new_file.count("/")

    if count_of_dir == 0:
        os.rename(file_name, path_new_file)
    if count_of_dir > 0:
        folders = path_new_file.split("/")
        new_file_name = folders.pop()
        path_file = "/".join(folders)
        os.makedirs(path_file)
        with open(f"{file_name}", "r") as file_in,\
                open(os.path.join(path_file, new_file_name), "w") as file_out:
            file_out.write(file_in.read())
        os.remove(file_name)
