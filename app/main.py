import os


def move_file(command: str) -> None:
    _, copied_file, file_to_copy = command.split()
    directory = file_to_copy.split("/")
    path = directory[0]
    os.mkdir(path)
    for index in range(1, len(directory) - 1):
        path += "/" + directory[index]
        os.mkdir(path)

    with open(copied_file, "r") as file_in, \
            open(file_to_copy, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(copied_file)
