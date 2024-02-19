import shutil
import os


def move_file(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise ValueError("Please, input correct request")
    cmnd, file1, file2 = command.split()
    if cmnd == "mv" and file1 != file2:
        file2 = file2.split("/")
        temp = ""
        while len(file2) > 1:
            temp += file2[0]
            try:
                os.makedirs(temp)
            except FileExistsError:
                pass
            temp += "/"
            file2.pop(0)
        file2 = temp + str(file2[0])
        shutil.move(file1, file2)
