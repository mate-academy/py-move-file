import os


def move_file(command: str):
    file_name = command.split()[1]
    new_file_name = command.split("/")[-1]
    with open(file_name, "r") as file:
        path = ""
        for directory in command.split()[2].split("/")[:-1]:
            path += directory + "/"
            os.mkdir(path)
        with open(path + new_file_name, "w") as new_file:
            new_file.write(file.read())
    os.remove(file_name)
