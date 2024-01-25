import os


def move_file(command: str) -> None:
    file, path_to_move = command[3:].split(" ")
    directories = path_to_move.split("/")

    with open(file, "r") as r:
        content = r.read()

        path_without_file = os.path.join(directories[:-1])
        if os.path.isdir(path_without_file):
            with open(path_to_move, "w") as a:
                a.write(content)

        else:
            if directories[:-1]:
                os.makedirs(path_without_file, exist_ok=True)

            with open(path_to_move, "a") as a:
                a.write(content)

    os.remove(file)
