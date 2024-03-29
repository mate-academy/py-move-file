import os


def move_file(command: str) -> None:
    _, source_file, destination_path = command.split()
    if "/" in destination_path:
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    with open(source_file, "r") as src, open(destination_path, "w") as dst:
        dst.write(src.read())
    os.remove(source_file)
