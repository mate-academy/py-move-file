import os


class BadCommand(Exception):
    """Invalid command"""


def move_file(command: str):
    move_command = command.split(" ")[0]
    file_name = command.split(" ")[1]
    new_file_name = command.split(" ")[2]

    # command checking
    if move_command != "mv":
        raise BadCommand("Invalid command")

    # making directories
    if "/" in new_file_name:
        path_list = new_file_name.split("/")
        path = path_list[0]
        for i in range(len(path_list) - 1):
            os.mkdir(path)
            path = f"{path}/{path_list[i + 1]}"

    # copy file
    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())

    # delete old file
    os.remove(file_name)
