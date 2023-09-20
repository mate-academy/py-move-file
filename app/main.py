import os


def move_file(command: str) -> None:
    file_names = command.split(" ")

    if file_names[0] != "mv" or len(file_names) != 3:
        return
    with open(file_names[1], "r") as file:
        text = file.read()
    os.remove(file_names[1])

    file_path = file_names[2].split("/")
    current = ""

    for directory in file_path[:-1]:
        current += directory + "/"
        if not os.path.exists(current):
            os.mkdir(current)

    with open(file_names[2], "w") as file:
        file.write(text)
