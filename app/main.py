from os import remove, makedirs


def move_file(command):
    old_file_name = command.split()[1]
    path_to_move = command.split()[2]

    old_file = open(old_file_name, "r")
    dirs = path_to_move.split("/")[:-1]
    path_without_file = "/".join(dirs)

    if len(path_to_move.split("/")) > 1:
        makedirs(path_without_file)

    new_file = open(path_to_move, "w")

    for data in old_file.readlines():
        new_file.write(data)

    old_file.close()
    new_file.close()
    remove(old_file_name)
