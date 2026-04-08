import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if source == destination:
        return

    if destination.endswith("/") or destination.endswith("\\"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    directory = os.path.dirname(destination)

    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    if os.path.exists(source):
        with open(source, "r") as f_src, open(destination, "w") as f_dst:
            f_dst.write(f_src.read())

        os.remove(source)
