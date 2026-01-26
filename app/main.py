import os


def move_file(command: str) -> None:
    command_list = command.split()
    addres_list = command_list[2].split("/")
    full_addres = ""
    if len(command_list) != 3:
        return None
    if command_list[0] != "mv":
        return None
    else:
        if command_list[2] == addres_list[0]:
            os.rename(command_list[1], addres_list[0])
        else:
            for name_directory in addres_list[:-1]:
                full_addres = os.path.join(full_addres, name_directory)
                try:
                    os.mkdir(full_addres)
                except FileExistsError:
                    pass
            with open(command_list[2], "w") as new_file:
                new_file.write(open(command_list[1], "r").read())
                new_file.close()
                os.remove(command_list[1])
