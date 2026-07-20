import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in format: mv <source> <destination>"
        )

    _, source, destination = parts
    path_parts = destination.split("/")

    if destination.endswith("/"):
        path_parts[-1] = os.path.basename(source)

    with open(source, "r") as source_file:
        content = source_file.read()

    current_path = ""

    for directory in path_parts[:-1]:
        current_path = os.path.join(current_path, directory)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    destination_path = os.path.join(current_path, path_parts[-1])

    with open(destination_path, "w") as new_file:
        new_file.write(content)

    os.remove(source)
