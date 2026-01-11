import os


def move_file(command: str) -> None:
    old_file = command.split()[1]
    new_file = command.split()[2]
    command = command.split()[0]

    if command != "mv" or new_file[-1] == "/":
        print("Incorrect command")
        return

    with open(old_file) as source:
        data = source.read()

    path = new_file.split("/")
    directory = ""

    for folder in path[:-1]:
        directory = os.path.join(directory, folder)
        if not os.path.isdir(directory):
            os.mkdir(directory)

    new_file = os.path.join(directory, path[-1])

    with open(new_file, "w") as copy:
        copy.write(data)

    os.remove(old_file)
