import os


def move_file(command: str) -> None:
    split_command = command.split()
    path_elements = None
    if "/" in split_command[2]:
        path_elements = split_command[2].split("/")
    path = ""
    for element in path_elements:
        if "." not in element:
            path += element + "/"
            os.mkdir(path)
    with open(split_command[1], "r") as source,\
            open(split_command[2], "w") as copy:
        source_content = source.read()
        copy.write(source_content)
    os.remove(split_command[1])
