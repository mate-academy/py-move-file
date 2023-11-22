import os


def move_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination = parts[2]
    if parts[1] == parts[2]:
        return
    directory, file_name = os.path.split(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source_file, "r") as src, open(destination, "w") as dst:
        dst.write(src.read())
    os.remove(source_file)
