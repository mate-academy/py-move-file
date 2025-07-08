import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: 'mv source destination'"
        )

    _, source_file, destination = parts

    if not os.path.exists(source_file):
        raise FileNotFoundError(
            f"Source file '{source_file}' does not exist"
        )

    if not os.path.isfile(source_file):
        raise ValueError(f"Source '{source_file}' is not a file")

    if destination.endswith("/"):
        dest_dir = destination
        dest_file = os.path.join(dest_dir, os.path.basename(source_file))
    else:
        dest_dir = os.path.dirname(destination)
        dest_file = destination

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(source_file, "r") as f:
        content = f.read()

    with open(dest_file, "w") as f:
        f.write(content)

    os.remove(source_file)
