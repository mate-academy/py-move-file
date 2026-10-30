import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    try:
        with open(source_path, "r") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        return

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path,
            os.path.basename(source_path)
        )

    directory = os.path.dirname(destination_path)

    if directory:
        current_path = ""

        for folder in directory.split(os.sep):
            if not folder:
                continue

            current_path = os.path.join(current_path, folder)

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
