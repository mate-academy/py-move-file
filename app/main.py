import os


def move_file(command: str) -> None:
    mv, source_file, new_file = command.split()

    if mv == "mv":
        file_name = new_file.split("/")[-1]
        parent_dir = ""
        path = ""
        for directory in new_file.split("/")[:-1]:
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            parent_dir += directory + "/"

        with open(source_file, "r") as source, \
                open(os.path.join(path, file_name), "w") as new:
            new.write(source.read())
        os.remove(source_file)
