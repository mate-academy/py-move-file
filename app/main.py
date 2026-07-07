import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)
    if dest_dir and not os.path.exists(dest_dir):
        path_parts = dest_dir.split(os.sep)
        current_path = ""
        for part in path_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    if dest_dir and not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
