import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use 'mv source destination'")
    source = parts[1]
    destination = parts[2]
    if not os.path.isfile(source):
        raise FileNotFoundError(f"File {source} not found.")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

    with (open(source, "r") as source_file,
          open(destination, "w") as destination_file):
        destination_file.write(source_file.read())

    os.remove(source)
