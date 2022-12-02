import os


def move_file(command: str) -> None:
    new_list = command.split()
    file_name = new_list[1]
    copy_name = new_list[2]

    try:
        copy_name.index("/")
    except ValueError:
        os.rename(file_name, copy_name)

    path_keys = copy_name.split("/")
    path = ""

    for i in range(len(path_keys) - 1):
        os.mkdir(path + path_keys[i])
        path += path_keys[i] + "/"

    file_path = path + path_keys[-1]

    with open(file_name, "r") as file, open(path_keys[-1], "w") as copy:
        copy.write(file.read())

    os.replace(path_keys[-1], file_path)
    os.remove(file_name)
