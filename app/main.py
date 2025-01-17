import os


def move_file(command: str) -> None:
    parts = command.split(" ", 2)
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: "
            "'mv <source> <destination>'")

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' not found.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

    os.rename(source, destination)

    print(f"Moved '{source}' to '{destination}'")
