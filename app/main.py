import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>"
        )
    source_filename: str = parts[1]

    if parts[2].endswith("/"):
        destination_filename = source_filename
        destination_path = parts[2].rstrip("/")
    else:
        destination_path = os.path.dirname(parts[2])
        destination_filename = parts[2]

    if destination_path:
        os.makedirs(destination_path, exist_ok=True)

    with (
        open(source_filename, "r") as source_file,
        open(destination_filename, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_filename)
