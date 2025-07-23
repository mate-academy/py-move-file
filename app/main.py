import os


def move_file(command: str) -> None:
    command_lst = command.split()
    if len(command_lst) != 3:
        return
    mv, old_file, directory = command_lst

    if mv != "mv":
        return
    if old_file == directory:
        return
    if not os.path.isfile(old_file):
        return

    if "/" not in directory:
        copy_file(old_file, directory)
    else:
        directory_list = directory.split("/")
        for i in range(1, len(directory_list)):
            current_directory = "/".join(directory_list[:i])
            if not os.path.isdir(current_directory):
                os.mkdir(current_directory)
        copy_file(old_file, directory)


def copy_file(old_file: str, new_file: str) -> None:
    with open(old_file, "r") as old , open(new_file, "w") as new:
        new.write(old.read())
    os.remove(old_file)
