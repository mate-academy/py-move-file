import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must have exactly 3 elements: mv <source> <destination>"
        )
    _, source_path, destination_path = parts

    if destination_path.endswith("/") or (
        os.sep != "/" and destination_path.endswith(os.sep)
    ):
        destination_dir = destination_path.rstrip("/").rstrip(os.sep)
        destination_path = os.path.join(
            destination_dir, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
