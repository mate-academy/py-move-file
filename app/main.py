import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]
    if not os.path.isfile(source):
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
