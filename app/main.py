import os


def move_file(command: str) -> None:
    cmd, file_1, file_2 = command.split()
    if cmd != "mv":
        print('only "mv" command is supported')
        return None
    if "/" not in file_2:
        os.rename(file_1, file_2)
    else:
        os.makedirs(os.path.dirname(file_2))
        with open(file_1, "r") as f1, open(file_2, "w") as f2:
            f2.write(f1.read())
        os.remove(file_1)
