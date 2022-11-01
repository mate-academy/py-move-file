import os


def copy_file(filename: str, new_file: str) -> None:
    with open(filename, "r") as file_in,\
            open(new_file, "w") as file_out:
        file_out.write(file_in.read())


def move_file(command: str) -> None:
    if "mv" in command:
        filename = command.split()[1]
        path = command.split()[2].split("/")[:-1]
        new_filename = command.split()[2]
        directory = ""
        for i in range(len(path)):
            directory = os.path.join(directory, path[i])
            if not os.path.isfile(directory):
                os.mkdir(directory)
        copy_file(filename, new_filename)
        os.remove(filename)
