import os


def move_file(command):
    old_file_name = command.split(" ")[1]
    new_file_path = command.split(" ")[2]
    if "/" not in new_file_path:
        os.renames(old_file_name, new_file_path)
    else:
        dirc = new_file_path.split("/")
        os.makedirs("/".join(dirc[:-1]))
        with open(old_file_name, "r") as old_file,\
                open(new_file_path, "w") as new_file:
            for info in old_file.read():
                new_file.write(info)
    os.remove(old_file_name)
