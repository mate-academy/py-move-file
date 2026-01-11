import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    move, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' not found")

    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with (
        open(source, "r") as file_in,
        open(destination, "w") as file_out
    ):
        file_out.write(file_in.read())
    os.remove(source)
