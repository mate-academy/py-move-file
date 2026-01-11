import os


def move_file(command: str) -> None:
    command_ls = command.split()
    if len(command_ls) == 3 and \
            command_ls[0] == "mv" and \
            command_ls[1] != command_ls[2] and \
            command_ls[2][-1] != "/":

        dir_ls = command_ls[2].split("/")
        cur_path = os.getcwd()

        for idx in range(len(dir_ls) - 1):
            cur_path = os.path.join(cur_path, dir_ls[idx])
            if not os.path.exists(cur_path):
                os.mkdir(cur_path)

        if os.path.exists(command_ls[1]):
            with open(command_ls[1], "r") as file_in, \
                    open(command_ls[2], "w") as file_out:
                file_out.writelines(file_in.readlines())

            os.remove(command_ls[1])
