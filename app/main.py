import os


def move_file(command: str) -> None:
    """Moves a file to a new location or renames it, like Linux 'mv'."""
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path, destination_path = parts[1], parts[2]

    if not os.path.exists(source_path):
        return

    # Handle case when destination is a directory
    if destination_path.endswith(os.sep):
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    else:
        dir_name = os.path.dirname(destination_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

    with open(source_path, "r", encoding="utf-8") as src, open(
        destination_path, "w", encoding="utf-8"
    ) as dst:
        dst.write(src.read())

    os.remove(source_path)
