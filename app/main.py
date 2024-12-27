import os


def move_file(command: str) -> None:
    file_name, new_path = command.split(" ")[1:]

    with open(file_name, "r") as sorce:
        text = sorce.read()

    os.remove(file_name)
    dir_list = new_path.split("/")
    directory = ""

    for index in range(len(dir_list) - 1):
        if index:
            directory += "/" + dir_list[index]
        else:
            directory += dir_list[index]
        if os.path.exists(directory):
            continue
        os.mkdir(directory)

    with open(new_path, "w") as new_file:
        new_file.write(text)
