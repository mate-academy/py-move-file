import os


def move_file(command: str) -> None:
    cmd, file_1, file_2 = command.split()
    if cmd != "mv":
        print('only "mv" command is supported')
        return None
    if "/" not in file_2:
        os.rename(file_1, file_2)
    else:
        dir_list = file_2.split("/")[0:-1]
        os.mkdir(dir_list[0])
        if len(dir_list) >= 2:
            for i in range(len(dir_list[0:-1])):
                os.mkdir(f"{"/".join(file_2.split("/")[0:i + 1])}"
                         f"/{dir_list[i + 1]}")
        with open(file_1, "r") as f1, open(file_2, "w") as f2:
            f2.write(f1.read())
        os.remove(file_1)
