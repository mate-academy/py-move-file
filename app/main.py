import os


def move_file(command: str):
    parsed = command.split()

    if parsed[0] == "mv" and parsed[1] != parsed[2]:
        if os.path.isfile(parsed[2]):
            return

        if parsed[2][-1] == os.path.sep:
            parsed[2] += parsed[1]

        path = ""
        for d in parsed[2].split(os.path.sep)[:-1]:
            if not os.path.isdir(path + d):
                os.mkdir(path + d)
                path += d + os.path.sep

        os.rename(parsed[1], parsed[2])
