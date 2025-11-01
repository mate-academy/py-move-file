import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3:
        return

    cmd, source_file_name, destination_path = parts
    if cmd != "mv":
        return

    if destination_path.endswith(os.path.sep):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file_name)
        )

    if os.path.abspath(source_file_name) == os.path.abspath(destination_path):
        return

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)

    with (open(source_file_name, "rb") as source_file,
          open(destination_path, "wb") as destination_file):
        while True:
            chunk = source_file.read(1024 * 1024)
            if not chunk:
                break
            destination_file.write(chunk)

    os.remove(source_file_name)
