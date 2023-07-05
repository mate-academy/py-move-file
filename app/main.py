from os import mkdir, remove, path


def move_file(command: str) -> None:
    sep_command = command.split()

    file_in = sep_command[1]
    file_out = sep_command[2]
    dir_list = sep_command[2].split("/")
    dir_list.pop()

    if "/" in command:
        pth = ""
        for drc in dir_list:
            pth += drc
            if path.exists(pth):
                pth += "/"
                continue
            mkdir(pth)
            pth += "/"

    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())

    remove(file_in)
