import os


def move_file(command):
    origin = command.split(" ")[1]  # source file_name
    if "/" not in command:  # check if we need just rename file
        os.rename(origin, command.split(" ")[2])
    else:
        dirs_copy = command.split(" ")[2]  # list with dirs and copy_file
        copy = dirs_copy.split["/"][-1]  # copy_file name
        dirs = dirs_copy.split("/")[:-1]  # list of dirs
        if len(dirs) == 1:  # check how many dirs we have to created
            os.mkdir(dirs)
            with open(origin, "r") as file_in, \
                    open(dirs + "/" + copy, "w") as file_out:
                file_out.write(file_in.read())
                os.remove(origin)
        else:
            path = "/".join(dirs)
            os.makedirs(path)
            with open(origin, "r") as file_in, \
                    open(path + "/" + copy, "w") as file_out:
                file_out.write(file_in.read())
                os.remove(origin)
