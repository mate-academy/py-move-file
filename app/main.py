import os


def move_file(commands: str) -> object:
    command, file, directory = commands.split()
    if command == "mv":
        if "/" not in directory:
            os.rename(file, directory)
            return

        *path, file1 = directory.split("/")
        direct = "/".join(path)
        if not os.path.exists(direct):
            os.makedirs(direct)
        moved_direct = os.path.join(direct, file1)
        with open(moved_direct, "w") as filename, open(file, "r") as source:
            filename.write(source.read())

        os.remove(file)
