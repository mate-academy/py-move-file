import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv source_file destination"
        )

    source = parts[1]
    destination = parts[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f'No such file: "{source}"')

    if destination.endswith("/"):
        if not os.path.exists(destination):
            os.makedirs(destination)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

    os.rename(source, destination)
