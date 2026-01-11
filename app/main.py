from os import remove, makedirs


def move_file(command: str):
    source = command.split(" ")[1]
    path_list = command.split(" ")[2]
    path = "/".join(path_list.split("/")[0:-1])
    with open(source, "r") as original:
        content = original.read()
    makedirs(path)
    with open(path_list, "w") as new_file:
        new_file.write(content)
    remove(source)





