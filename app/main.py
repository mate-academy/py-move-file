import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file_name, destination_file_name = parts

    if (
        destination_file_name.endswith(os.sep)
        or destination_file_name.endswith("/")
    ):
        destination_file_name = os.path.join(
            destination_file_name,
            os.path.basename(source_file_name)
        )

    destination_dir = os.path.dirname(destination_file_name)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source_file_name, "r") as source_file:
        content = source_file.read()

    with open(destination_file_name, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_file_name)
