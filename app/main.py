import os


def move_file(command: str) -> None:
    parts: list[str] = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source: str = parts[1]
    destination: str = parts[2]

    if source == destination:
        return

    if destination.endswith("/"):
        file_name: str = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    target_dir: str = os.path.dirname(destination)

    try:
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(source)

    except (FileNotFoundError, PermissionError, OSError):
        return
