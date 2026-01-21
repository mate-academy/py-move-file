import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>"
        )

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

    os.rename(source, destination)
