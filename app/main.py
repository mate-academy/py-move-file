import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv <source> <destination>")
    source, destination = parts[1], parts[2]
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    destination_dir = os.path.dirname(destination)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    with open(source, "r") as src_file:
        with open(destination, "w") as dest_file:
            dest_file.write(src_file.read())
    os.remove(source)
