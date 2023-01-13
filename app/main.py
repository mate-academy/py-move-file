import os.path


def move_file(command: str) -> None:
    mv, source_f, directories_new = command.split()
    if mv == "mv":
        directories, new = os.path.split(directories_new)
        os.makedirs(directories)
        with open(source_f, "r") as source, open(new, "w") as new_file:
            new_file.write(source.read())
        os.remove(source_f)
