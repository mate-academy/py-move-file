import os


def move_file(command: str) -> None:
    method, filename, dir_file = command.split()
    dir_file_split = dir_file.split("/")

    if method != "mv" or filename == dir_file:
        return

    new_path = ""

    for path in dir_file_split[:-1]:
        new_path = os.path.join(new_path, path)
    os.mkdir(new_path)

    with open(filename, "r") as file_in,\
            open(dir_file_split[-1], "w") as file_out:
        file_out.write(file_in.read())
        os.remove(filename)
