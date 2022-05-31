import os


def move_file(command):
    old_file = command.split()[1]
    new_file = command.split()[2]
    directories = new_file.split("/")[:-1]

    if command != "mv":
        raise ValueError("Wrong command.")

    directory_to_add = ""
    for directory in directories:
        directory_to_add += directory + "/"
        os.mkdir(directory_to_add)

    with open(old_file, "r") as f_old:
        content = f_old.read()
        with open(new_file, "w") as f_new:
            f_new.write(content)

    os.remove(old_file)
