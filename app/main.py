import os


def move_file(command: str) -> None:
    command, file, path = command.split()
    if command != "mv":
        raise Exception("please enter command 'mv'")
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(file) as file_1, open(path, "w") as file_2:
        text = file_1.read()
        file_2.write(text)
    os.remove(file)
