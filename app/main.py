import os


def move_file(command):
    if command.split()[0] == "mv":
        file = command.split()[1]
        path = command.split()[2]
        new_file = path.split("/")[-1]
        path = path.replace(new_file, "")
        new_path = os.path.join(path)
        os.makedirs(new_path)
        with open(file, "r") as source_file:
            file_copy = source_file.read()
        os.remove(file)
        os.chdir(new_path)
        with open(new_file, "w") as new_file:
            new_file.write(file_copy)
