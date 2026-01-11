import os


def move_file(command: str) -> None:
    command_, filename, some_dir_newfile = command.split()
    if command_ == "mv":
        if "/" in command:
            dir_ls = some_dir_newfile.split("/")[:-1]
            path = ""
            for directory in dir_ls:
                os.mkdir(path + str(directory))
                path += str(directory) + "/"

            with open(filename, "r") as file_in, \
                    open(some_dir_newfile, "w") as file_out:
                file_out.write(file_in.read())

            os.remove(filename)
        else:
            os.rename(filename, some_dir_newfile)
