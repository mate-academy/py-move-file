import os
import pathlib


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3:
        cmd, file1, file2 = command
        if cmd != "mv":
            return
        if "/" not in file2:
            with open(file1, "r") as file_1, open(file2, "w") as file_2:
                file_2.write(file_1.read())
        else:
            file2 = file2.split("/")
            path = str(pathlib.Path().absolute()) + "/"
            file2 = file2[-1]
            for i in range(len(file2) - 1):
                path += file2[i] + "/"
            file2 = os.path.join(path, file2)
            os.makedirs(path)
            with open(file1, "r") as file_1, open(file2, "w") as file_2:
                file_2.write(file_1.read())

        os.remove(file1)
