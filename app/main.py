import os


def move_file(command: str) -> None:
    parts = command.split()
    command, source, target = parts
    if any([len(parts) != 3, command != "mv", source == target]):
        return
    if os.path.dirname(target) != "" or target.endswith("/"):
        os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(source, "r") as file1, open(target, "w") as file2:
        file2.write(file1.read())
    os.remove(source)
