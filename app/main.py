import os


def move_file(command: str):
    ls = command.split(" ")
    sourcefile = ls[1]
    destination = ls[2].split("/")
    if len(destination) == 1:
        with open(sourcefile) as f:
            lines = f.readlines()
        with open(destination[0], "a") as f1:
            f1.writelines(lines)
    else:
        copyfile = ""
        if len(destination[-1]) != 0:
            copyfile = destination[-1]
        directory = destination[0:-1]
        adpath = ""
        for i in directory:
            adpath += i
            os.mkdir(adpath)
            adpath += "/"
        with open(sourcefile) as f:
            lines = f.readlines()
        if len(destination[-1]) != 0:
            with open(os.path.join(*directory, copyfile), "a") as f1:
                f1.writelines(lines)
        else:
            with open(os.path.join(*directory, sourcefile), "a") as f1:
                f1.writelines(lines)

    os.remove(sourcefile)

move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
