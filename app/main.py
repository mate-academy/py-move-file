from os import mkdir, remove


def move_file(command: str):
    dir_list = []
    file_name_in = command.split()[1]
    second_arg = command.split()[2]

    if "/" in second_arg:
        dir_list = second_arg.split("/")
        if second_arg[-1] != "/":
            file_name_out = dir_list.pop()
        else:
            file_name_out = file_name_in
    else:
        file_name_out = second_arg

    for i in range(1, len(dir_list)):
        dir_list[i] = "/".join(dir_list[i - 1: i + 1])

    for dir_new in dir_list:
        try:
            mkdir(dir_new)
        except FileExistsError:
            pass

    if len(dir_list) > 0:
        file_name_out = f"{dir_list[-1]}/{file_name_out}"

    with open(file_name_in, "r") as file_in, \
            open(file_name_out, "w") as file_out:
        file_out.write(file_in.read())
        file_in.close()
        remove(file_name_in)
