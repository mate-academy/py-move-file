import os


def move_file(command: str) -> None:
    command, filename, path = command.split()
    dirs = os.path.dirname(path)

    if command == "mv":
        if dirs:
            os.makedirs(dirs, exist_ok=True)

        with open(filename, "r") as file_to_move:
            with open(path, "w") as new_file:
                new_file.write(file_to_move.read())

        os.remove(filename)
