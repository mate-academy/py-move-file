from os import remove, makedirs


def move_file(command):
    old_file_name = command.split()[1]
    path_to_move = command.split()[2]
    with open(old_file_name, "r") as old_file:

        dirs = path_to_move.split("/")[:-1]
        path_without_file = "/".join(dirs)

        if len(path_to_move.split("/")) > 1:
            makedirs(path_without_file)

        with open(path_to_move, "w") as new_file:
            for data in old_file.readlines():
                new_file.write(data)

    remove(old_file_name)
