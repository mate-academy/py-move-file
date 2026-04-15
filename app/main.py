import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

    if (
            destination.endswith("/")
            or destination.endswith("\\")
            or destination.endswith(os.sep)
    ):
        destination = os.path.join(destination, os.path.basename(source))

    directory_path = os.path.dirname(destination)

    if directory_path:
        norm_path = directory_path.replace("/", os.sep)
        norm_path = norm_path.replace("\\", os.sep)

        path_parts = norm_path.split(os.sep)
        current_path = ""

        for part in path_parts:
            if not part:
                if not current_path:
                    current_path = os.sep
                continue

            current_path = os.path.join(current_path, part)

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as src_file:
        content = src_file.read()

    with open(destination, "w") as dest_file:
        dest_file.write(content)

    os.remove(source)
