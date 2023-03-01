from os import remove, mkdir


def move_file(command: str):
    command, old_file_name, new_position = command.split()

    if command != "mv":
        raise ValueError("We need mv command to move file")

    *folders, new_file_name = new_position.split("/")
    directory = ""

    for folder in folders:
        directory += folder + "/"
        mkdir(directory)

    with open(old_file_name, "r") as old_file:
        with open(directory + new_file_name, "w") as new_file:
            new_file.write(old_file.read())

    remove(old_file_name)
