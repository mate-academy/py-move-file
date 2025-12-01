import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if destination.endswith("/"):
        source_filename = os.path.basename(source)
        destination = os.path.join(destination, source_filename)

    dir_path = os.path.dirname(destination)

    if dir_path:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    with open(source, "r") as file1, open(destination, "w") as file2:
        content = file1.read()
        file2.write(content)

    os.remove(source)
