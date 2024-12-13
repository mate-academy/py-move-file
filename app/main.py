from os import mkdir, remove, path


def move_file(command):
    files_paths = command.split(" ")[1::]
    old_file_path = files_paths[0]
    new_file_path = files_paths[1]
    if "/" in new_file_path:
        file_path = new_file_path.split("/")[:-1:]
        file_path_string = ""
        for direction in file_path:
            file_path_string += f"{direction}/"
            if not path.isdir(file_path_string):
                mkdir(file_path_string)

    with open(old_file_path, "r") as old_file:
        with open(new_file_path, "w") as new_file:
            new_file.write(old_file.read())
    remove(old_file_path)
