import os


def move_file(command: str) -> None:
    split_command_list = command.split()

    old_file = split_command_list[1]
    list_of_names = split_command_list[2].split("/")
    new_dir = "/".join(list_of_names[:-1])
    os.makedirs(new_dir)
    new_file = "/".join(list_of_names)

    with open(old_file, "r") as old_file:
        with open(new_file, "a") as new_file:
            new_file.writelines(old_file.readlines())
    os.remove(old_file)
    