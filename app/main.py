import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source, destination = parts
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with (open(source, "r") as source_file,
          open(destination, "w") as destination_file):
        destination_file.write(source_file.read())
    os.remove(source)
