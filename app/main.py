import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in the format: 'mv <source> <destination>'"
        )

    source, destination = parts[1], parts[2]

    if destination.endswith("/"):
        destination_dir = destination.rstrip("/")
        destination_filename = os.path.basename(source)
        destination_path = os.path.join(destination_dir, destination_filename)
    else:
        destination_path = destination
        destination_dir = os.path.dirname(destination_path)

    path = ""
    for part in destination_dir.split("/"):
        if part:
            path = os.path.join(path, part)
            if not os.path.exists(path):
                os.mkdir(path)

    with open(source, "r") as src, open(destination_path, "w") as dst:
        dst.write(src.read())

    os.remove(source)
