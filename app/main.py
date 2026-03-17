import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source, destination = parts[1], parts[2]
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r", encoding="utf-8") as file_in, open(
        destination, "w", encoding="utf-8"
    ) as file_out:
        file_out.write(file_in.read())

    os.remove(source)
