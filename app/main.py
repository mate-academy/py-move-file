import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv <source> <destination>")

    _, source, destination = parts

    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    if destination.endswith(os.sep):
        destination_dir = destination.rstrip(os.sep)
        file_name = os.path.basename(source)
        destination = os.path.join(destination_dir, file_name)
    else:
        destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    os.rename(source, destination)
