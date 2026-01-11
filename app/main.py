from os import mkdir, remove


def move_file(command):
    files_way = command.split(" ")[1:]
    first_file = files_way[0]
    second_file = files_way[1]
    file_path = second_file.split("/")[:-1]
    file_path_s = ""
    for directory in file_path:
        file_path_s += f"{directory}/"
        mkdir(file_path_s)
    with open(first_file, "r") as old_file:
        with open(second_file, "w") as new_file:
            new_file.write(old_file.read())
    remove(first_file)
