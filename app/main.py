import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "mv":
        new_path = command_list[2].split("/")
        dir_file = ""
        for i in range(len(new_path) - 1):
            dir_file = dir_file + new_path[i]
            if not os.path.exists(dir_file):
                os.mkdir(dir_file)
            dir_file = dir_file + "/"

    with (open(command_list[1], "r") as file_out,
          open(command_list[2], "w") as file_in):
        file_in.write(file_out.read())

    os.remove(command_list[1])
