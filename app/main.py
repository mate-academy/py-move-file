import os


def move_file(command: str) -> None:
    cmd, file1, file2 = command.split()
    if cmd == "mv" and file1 != file2:
        path_to_file = file2.split("/")
        if len(path_to_file) > 1:
            name_dir = path_to_file[0]
            os.mkdir(name_dir)
            for i in range(1, len(path_to_file) - 1):
                name_dir = name_dir + "/" + path_to_file[i]
                os.mkdir(name_dir)
        with open(file1, "r") as file_in, \
             open(file2, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(file1)
