import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_file, destination_path = parts[1], parts[2]

    if not os.path.isfile(source_file):
        return

    if destination_path[-1] == "/":
        destination_dir = destination_path
        destination_file = os.path.join(
            destination_dir, os.path.basename(source_file)
        )
    else:
        destination_dir = os.path.dirname(destination_path)
        destination_file = destination_path

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    os.rename(source_file, destination_file)
