import os


def move_file(command: str) -> None:
    mv, source_file, new_file = command.split()
    if mv == "mv" and "/" not in new_file:
        with open(source_file, "r") as source, open(new_file, "w") as copy:
            copy.write(source.read())
        os.remove(source_file)
    elif mv == "mv" and "/" in new_file:
        creating_file = new_file.split("/")[-1]
        directories = new_file.split("/")[:-1]
        parent_dir = ""
        path = ""
        for directory in directories:
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            parent_dir += directory + "/"
        path_to_file = os.path.join(path, creating_file)
        with open(source_file, "r") as source, \
                open(path_to_file, "w") as copy:
            copy.write(source.read())
        os.remove(source_file)
