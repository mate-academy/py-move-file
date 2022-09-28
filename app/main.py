from os import remove, mkdir


def move_file(command):
    command, file1, file2 = command.split()
    if command == "mv" and len(file2.split("/")) > 1:
        for i in range(len(file2.split("/") - 1)):
            mkdir(file2.split("/")[i])
    with open(file1, "r") as f1, open(file2, "w") as f2:
        f2.write(f1.read())

    remove(file1)
