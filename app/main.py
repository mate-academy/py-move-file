import os


def move_file(command: str):
    operator, old_file_name, destination = command.split()
    *folders, new_file_name = destination.split("/")

    if operator != "mv":
        return

    path = ""
    for folder_name in folders:
        path += folder_name + "/"
        os.mkdir(path)

    with open(old_file_name) as old_file:
        with open(path + new_file_name, "w") as new_file:
            new_file.write(old_file.read())

    os.remove(old_file_name)
