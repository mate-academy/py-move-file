import os


def move_file(command: str) -> None:
    if not command.startswith("mv "):
        raise ValueError(
            "Command must start with 'mv '."
            "")
    parts = command.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(
            "Invalid command format."
        )
    _, source, destination = parts
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file not found: {source}")
    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    os.rename(source, destination)
