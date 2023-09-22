import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    target = parts[2]
    if source == target:
        return

    if os.path.dirname(target) != "":
        os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(source, "r") as file1, open(target, "w") as file2:
        file2.write(file1.read())
    os.remove(source)
