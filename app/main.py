import os


def move_file(command: str) -> None:
    cmd, copy_from, copy_to = command.split(" ")

    if cmd != "mv":
        raise ValueError("Only 'mv' is possible")

    if "/" not in copy_to:
        copy_to_path = copy_to
    else:
        list_of_path = copy_to.split("/")
        file_name = list_of_path[-1]
        path_to_file = "/".join(list_of_path[:-1])

        if not os.path.exists(path_to_file):
            os.makedirs(path_to_file, exist_ok=True)

        copy_to_path = os.path.join(path_to_file, file_name)

    with open(copy_from, "r") as file_from:
        with open(copy_to_path, "w") as file_to:
            file_to.write(file_from.read())

    os.remove(copy_from)
