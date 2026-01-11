import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        raise ValueError("Command format is not correct")

    source_file, path = parts[1], parts[2]

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"No such file or directory: {source_file}")

    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
        path = os.path.join(path, os.path.basename(source_file))
    else:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)

    with open(source_file, "r") as source, open(path, "w") as destination_file:
        destination_file.write(source.read())
    os.remove(source_file)
