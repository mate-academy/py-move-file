import os


def move_file(command):
    origin = command.split(" ")[1]
    if "/" not in command:
        os.rename(origin, command.split(" ")[2])
    else:
        dirs_copy = command.split(" ")[2]
        copy = dirs_copy.split["/"][-1]
        dirs = dirs_copy.split("/")[:-1]
        if len(dirs) == 1:
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
