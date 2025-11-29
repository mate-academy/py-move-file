import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Expected: "
                         "'mv source destination'")

    _, source_path, destination_path = parts

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' does not exist")

    if not os.path.isfile(source_path):
        raise ValueError(f"Source '{source_path}' is not a file")

    if destination_path.endswith("/"):
        source_filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, source_filename)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
