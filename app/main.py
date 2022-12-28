import os


def move_file(command: str) -> None:
    file_name, path_with_file = command.lstrip("mv").split()
    new_file_name = path_with_file.split("/")[-1]
    prim_path = os.getcwd()
    new_path = "/".join(path_with_file.split("/")[:-1:])

    with open(file_name, "r") as prim_file:
        os.makedirs(new_path)
        os.chdir(new_path)
        with open(new_file_name, "w") as new_file:
            new_file.write(prim_file.read())

    os.chdir(prim_path)
    os.remove(file_name)
