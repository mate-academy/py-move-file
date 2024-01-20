import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    operation, file1, path_and_file2 = command.split()
    path = ""

    if "/" in path_and_file2:
        path = "/".join(path_and_file2.split("/")[:-1]) + "/"
        file_name = path + path_and_file2.split("/")[-1]
    else:
        file_name = path_and_file2

    if len(path) != 0:
        os.makedirs(path, exist_ok=True)

    with (
        open(file1, "r") as source,
        open(file_name, "w") as new_file
    ):
        new_file.write(source.read())

    os.remove(file1)
