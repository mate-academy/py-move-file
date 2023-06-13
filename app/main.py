import os


def move_file(command: str) -> None:
    command_list = command.split()

    if command_list[0] != "mv":
        return

    file_orig = command_list[1]
    file_copy = os.path.split(command_list[2])[-1]
    path = command_list[2].replace(file_copy, "")

    if path and not os.path.exists(path):
        os.makedirs(path)
        print("Directory not found. Creating directory")

    with open(file_orig, "r") as source, open(path + file_copy, "a+") as copy:
        copy.write(source.read())
    os.remove(file_orig)
