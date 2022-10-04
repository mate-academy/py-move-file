import os


def movie_file(command: str):
    command_list = command.split()
    if command_list[0] != "mv":
        return
    file1 = command_list[1]
    path = command_list[2].split("/")[:-1]
    file2 = "".join(command_list[2].split("/")[-1:])
    if len(path) == 0:
        os.rename(file1, file2)
        return
    elif len(path) == 1:
        os.mkdir(path[0])
    else:
        os.makedirs("/".join(path))
    with open(file1, "r") as file_in:
        with open(f"{"/".join(path)}/{file2}", "w") as file_out:
            file_out.writelines(file_in.readlines())
    os.remove(file1)
