import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
