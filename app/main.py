import os


def move_file(command: str) -> None:
    file, path_to_move = command[3:].split(" ")
    directories, filename = os.path.split(path_to_move)

    with open(file, "r") as r:
        content = r.read()

        if os.path.isdir(directories):
            with open(os.path.join(directories, filename), "w") as a:
                a.write(content)
        else:
            if directories:
                os.makedirs(directories, exist_ok=True)

            with open(path_to_move, "a") as a:
                a.write(content)

    os.remove(file)
