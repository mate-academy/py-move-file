import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(
            destination.rstrip("/"),
            os.path.basename(source)
        )

    path = os.path.dirname(destination)

    if path:
        os.makedirs(path, exist_ok=True)

    with open(destination, "w") as file1, open(source, "r") as file2:
        file1.write(file2.read())

    os.remove(source)
