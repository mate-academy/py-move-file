import os


def move_file(command: str):
    file = command.split()

    if file[0] == "mv" and file[1] != file[2]:
        if os.path.isfile(file[2]):
            return

        if file[2][-1] == os.path.sep:
            file[2] += file[1]

        path = ""
        for d in file[2].split(os.path.sep)[:-1]:
            if not os.path.isdir(path + d):
                os.mkdir(path + d)
                path += d + os.path.sep

        os.rename(file[1], file[2])
