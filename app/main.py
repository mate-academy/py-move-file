import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    source_file, path = parts[1], parts[2]

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' not found.")

    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
        destination = os.path.join(path, os.path.basename(source_file))
    else:
        destination_dir = os.path.dirname(path)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)
        destination = path

    with open(source_file, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source_file)
