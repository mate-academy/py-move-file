import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must contain exactly three parts: "
            "'mv', source, and destination"
        )

    _, source_file, destination = parts

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' does not exist")

    is_directory = os.path.isdir(destination) or destination.endswith("/")

    if is_directory:
        destination = destination.rstrip("/")
        destination_file = os.path.join(
            destination, os.path.basename(source_file)
        )
    else:
        destination_file = destination

    destination_dir = os.path.dirname(destination_file)

    if destination_dir:
        current_path = []

        for folder in destination_dir.split("/"):
            current_path.append(folder)
            path_to_create = os.path.join(*current_path)

            if not os.path.exists(path_to_create):
                os.mkdir(path_to_create)

    with open(source_file, "rb") as src, open(destination_file, "wb") as dst:
        dst.write(src.read())

    os.remove(source_file)
