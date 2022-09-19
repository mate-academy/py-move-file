import os


def move_file(command: str):
    command_list = command.split(" ")
    path_out_list = command_list[2].split("/")
    path = ""
    if len(path_out_list) > 1:
        for i in range(len(path_out_list) - 1):
            path += f"{path_out_list[i]}\\"
            if not os.path.isdir(path):
                os.mkdir(path)
    if path_out_list[-1] != "":
        with (open(command_list[1], "r") as file_in,
              open(path + path_out_list[-1], "w") as file_out):
            file_out.write(file_in.read())
    os.remove(command_list[1])
    return 0
