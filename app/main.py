import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    with open(source_path, "r") as source_file:
        content = source_file.read()

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_full_path = os.path.join(destination_path,
                                             os.path.basename(source_path))
    else:
        destination_dir = os.path.dirname(destination_path)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)
        destination_full_path = destination_path

    with open(destination_full_path, "w") as new_file:
        new_file.write(content)

    os.remove(source_path)
