import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    action, source_path, destination_path = parts

    if action != "mv" or not os.path.exists(source_path):
        return

    if destination_path.endswith("/"):
        source_file_name = os.path.basename(source_path)
        target_dir = destination_path.rstrip("/")
        target_path = os.path.join(target_dir, source_file_name)
    else:
        target_dir = os.path.dirname(destination_path)
        target_path = destination_path

    if source_path == target_path:
        return

    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    with (
        open(source_path, "r", encoding="utf-8") as source_file,
        open(target_path, "w", encoding="utf-8") as target_file,
    ):
        target_file.write(source_file.read())

    os.remove(source_path)
