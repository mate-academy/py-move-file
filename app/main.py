import os


def move_file(command: str) -> None:
    command = command.split()

    file2 = command[2].split("/")[-1]
    dir2 = command[2].replace(file2, "")

    if not os.path.exists(dir2) and dir2:
        os.makedirs(dir2)

    with open(command[1], "r") as f1, open(command[2], "w") as f2:
        f2.write(f1.read())
    os.remove(command[1])
