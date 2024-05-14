import os


def move_file(command_directory_file: str) -> None:
    data = command_directory_file.split()
    if len(data) == 3 and data[0] == "mv" and data[1] != data[2]:
        directory = os.path.dirname(data[2])
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(data[1], "r") as file_r, open(data[2], "w") as file_w:
            file_w.write(file_r.read())
        os.remove(data[1])
