import os


def move_file(command: str) -> None:
    _, file_name, path = command.split(" ")
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as new_file:
        with open(file_name, "r") as old_file:
            new_file.write(old_file.read())
        os.remove(file_name)
