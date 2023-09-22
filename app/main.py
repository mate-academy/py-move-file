import os


def move_file(command: str) -> None:
    parts = command.split()
    source, target = parts[1], parts[2]
    if len(parts) != 3 or parts[0] != "mv" or source == target:
        return

    if os.path.dirname(target) != "":
        os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(source, "r") as file1, open(target, "w") as file2:
        file2.write(file1.read())
    os.remove(source)
