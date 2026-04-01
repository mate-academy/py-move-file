import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3:
        raise ValueError("Invalid command format. "
                         "Usage: mv source destination")

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

    # Move the file
    os.rename(source, destination)
