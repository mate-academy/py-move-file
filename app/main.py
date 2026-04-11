import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source, destination = parts[1], parts[2]

    try:
        with open(source, "r") as f:
            data = f.read()
    except FileNotFoundError:
        return

    dir_path = os.path.dirname(destination)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(destination, "w") as f:
        f.write(data)

    os.remove(source)
