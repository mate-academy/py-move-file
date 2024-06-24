import os


def move_file(command: str) -> None:
    _, file, path = command.split()
    path = path.split("/")
    new_file = (os.path.join(*path) if len(path) == 1
                else os.path.join(*path[:-1]))
    if len(path) > 1:
        os.makedirs(new_file, exist_ok=True)
    with open(file) as file_1, open(new_file if len(path) == 1
                                    else os.path.join(new_file, path[-1]),
                                    "w") as file_2:
        text = file_1.read()
        file_2.write(text)
    os.remove(file)
