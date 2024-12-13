import os


def move_file(command: str) -> None:
    command_type, file_name, path_with_file = command.split()
    split_path = path_with_file.split("/")
    new_file_name = split_path[-1]
    primary_path = os.getcwd()
    new_path = "/".join(split_path[:-1:])

    with open(file_name, "r") as file:
        os.makedirs(new_path)
        os.chdir(new_path)
        with open(new_file_name, "w") as new_file:
            new_file.write(file.read())

    os.chdir(primary_path)
    os.remove(file_name)
