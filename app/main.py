import os


def move_file(command: str) -> None:
    command, old_file, list_of_names = command.split()

    list_of_names = list_of_names.split("/")
    new_dir = "/".join(list_of_names[:-1])
    os.makedirs(new_dir)
    new_file = "/".join(list_of_names)

    with open(old_file, "r") as old_file:
        with open(new_file, "a") as new_file:
            new_file.writelines(old_file.readlines())
    os.remove(old_file)
