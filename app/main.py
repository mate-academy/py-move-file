import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected format: 'mv source destination'"
        )

    _, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} does not exist")

    dest_dir = os.path.dirname(destination)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    os.rename(source, destination)
