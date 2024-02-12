import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[-1]

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))
    else:
        parent_dir = os.path.dirname(destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

    with open(source, "rb") as src_file:
        content = src_file.read()
    with open(destination, "wb") as dst_file:
        dst_file.write(content)

    os.rename(source, destination)
