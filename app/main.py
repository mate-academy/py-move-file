import os


def move_file(command: str) -> None:
    com = command.split()
    directory = com[2].split("/")
    path = directory[0]
    os.mkdir(path)
    for index in range(1, len(directory) - 1):
        path += "/" + directory[index]
        os.mkdir(path)

    with open(com[1], "r") as file_in, open(com[2], "w") as file_out:
        file_out.write(file_in.read())

    os.remove(com[1])
