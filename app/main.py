import os


def move_file(path: str) -> None:
    args = path.split()

    if len(args) != 3 or args[0] != "mv":
        return

    _, source, destination = args

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    folder_path = os.path.dirname(destination)

    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    with open(source, "r") as existing_file:
        source_content = existing_file.read()

    with open(destination, "w") as new_file:
        new_file.write(source_content)

    os.remove(source)
