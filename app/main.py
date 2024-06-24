import os


def move_file(command: str) -> None:
    command, file, path = command.split()
    if command != "mv":
        raise Exception("please enter command 'mv'")
    path = path.split("/")
    new_file = os.path.dirname(os.path.join(*path))
    if len(path) > 1:
        os.makedirs(new_file, exist_ok=True)
    with open(file) as file_1, open(os.path.join(new_file, path[-1]),
                                    "w") as file_2:
        text = file_1.read()
        file_2.write(text)
    os.remove(file)
