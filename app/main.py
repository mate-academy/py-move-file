import os


def move_file(command: str) -> None:
    func, file, directory = command.split()
    if "/" in command:
        command_ls = directory.split("/")
        for direc in command_ls[:-1]:
            os.mkdir(f"{directory[: directory.index(direc)]}{direc}")

        with open(file, "r") as source, open(directory, "w") as copy:
            copy.write(source.read())

        os.remove(file)
    else:
        os.rename(file, directory)
