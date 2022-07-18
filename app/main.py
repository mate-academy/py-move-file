import os


def move_file(command: str):
    old_file = command.split()[1]
    new_file = command.split()[2]
    address = ""
    if "/" in new_file:
        directories = new_file.split("/")[:-1]
        new_file = new_file.split("/")[-1]
        for directory in directories:
            os.mkdir(f"{address}{directory}")
            address += f"{directory}/"
    with open(old_file, "r") as file_in,\
            open(f"{address}{new_file}", "w") as file_out:
        file_out.write(file_in.read())
    os.remove(old_file)
