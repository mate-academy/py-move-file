import os


def copy_file(old_file_name: str, new_file_name: str) -> None:
    with (open(old_file_name, "r") as old_file,
          open(new_file_name, "w") as new_file):
        text = old_file.read()
        new_file.write(text)


def move_file(command: str) -> None:
    old_file_name = command.split(" ")[1]
    path_and_name = command.split(" ")[2]

    if "/" not in path_and_name:
        os.rename(old_file_name, path_and_name)
        return

    path_to_file = path_and_name.split("/")
    path = ""
    name = path_to_file[-1]
    for index in range(len(path_to_file) - 1):
        path += path_to_file[index]
        if not os.path.isdir(path):
            os.mkdir(path)
        path += "/"

    if name:
        # path = dir/new_name.txt
        copy_file(old_file_name, path + name)
    else:
        # path = dir/
        copy_file(old_file_name, path + old_file_name)
    os.remove(old_file_name)
