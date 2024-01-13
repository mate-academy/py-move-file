import os


def move_file(command: str) -> None:
    comm, filename, path = command.split()

    if comm != "mv":
        return

    dirs = "/".join(path.split("/")[:-1])

    if dirs:
        os.makedirs(dirs, exist_ok=True)

    with open(filename, "r") as file_to_move:
        with open(path, "w") as new_file:
            new_file.write(file_to_move.read())

    os.remove(filename)
