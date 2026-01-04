import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>"
        )
    _, source_filename, destination = parts

    if destination.endswith("/"):
        destination_path = destination.rstrip("/")
        destination_filename = os.path.join(
            destination_path,
            os.path.basename(source_filename)
        )
    else:
        destination_path = os.path.dirname(destination)
        destination_filename = destination

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)

    with (
        open(source_filename, "r") as source_file,
        open(destination_filename, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_filename)
