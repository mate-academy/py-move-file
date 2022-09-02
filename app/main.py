import os


def move_file(command: str):
    command, file_one, file_two = command.split(" ")
    if command == "mv":
        create_path(file_two)
        with open(file_one, "r") as f_one, open(file_two, "w") as f_two:
            content = f_one.read()
            f_two.write(content)  # copy content and delete current file
        os.remove(file_one)


def create_path(path_file):
    if "/" in path_file:
        path_two = path_file.split("/")[:-1]
        path = ""
        for p in path_two:  # create path by adding folders
            try:
                path += p + "/"
                os.mkdir(path)
            except FileExistsError:  # check if folder alredy present
                continue
