import os
import shutil


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, file1, file2 = parts

    if file1 == file2 or file2.endswith("/"):
        return

    directory = os.path.dirname(file2)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file1, "r") as f1, open(file2, "w") as f2:
        shutil.copyfileobj(f1, f2)

    os.remove(file1)
