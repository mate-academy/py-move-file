import os


def move_file(command: str) -> None:
    operators = command.split()
    if operators[0] != "mv":
        print("Wrong command!")
        return None
    filename = operators[1]
    path = operators[2].split("/")
    new_filename = path.pop()
    started_dir = os.getcwd()
    with open(filename, "r") as file, open(new_filename, "w") as new_file:
        for directory in path:
            try:
                os.mkdir(directory)
                os.chdir(directory)
            except FileExistsError:
                os.chdir(directory)
        new_file.write(file.read())
    os.chdir(started_dir)
    os.remove(filename)
