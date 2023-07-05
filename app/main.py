from os import makedirs, remove, path


def move_file(command: str) -> None:
    sep_command = command.split()

    if len(sep_command) != 3:
        print("Incorrect command!")

    file_in = sep_command[1]
    file_out = sep_command[2]
    dir_list = sep_command[2].split("/")
    dir_list.pop()

    if "/" in command:
        path_file_out = ""
        for drc in dir_list:
            path_file_out += drc
            if path.exists(path_file_out):
                path_file_out += "/"
                continue
            makedirs(path_file_out)
            path_file_out += "/"

    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())

    remove(file_in)
