import os


def move_file(command):
    sourse = command.split()[1]
    target = command.split()[2]

    if "/" in target:
        target_split = target.split("/")
        target_path = os.path.join(*target_split)

        os.makedirs("/".join(target.split("/")[:-1]))

        with open(target_path, "w") as f:
            f.write(open(sourse, "r").read())

        os.remove(sourse)
    else:
        os.rename(sourse, target)
