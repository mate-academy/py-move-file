import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv" and command[2][-1] != "/":

        with open(command[1]) as source:
            data = source.read()

        path = command[2].split("/")
        directory = ""

        for folder in path[:-1]:
            new_path = os.path.join(directory, folder)
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            directory = new_path
        new_file = os.path.join(directory, path[-1])

        with open(new_file, "w") as copy:
            copy.write(data)

        os.remove(command[1])
