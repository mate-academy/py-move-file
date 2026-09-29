import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return

    command_name, source_path, destination_path = command_parts
    if command_name != "mv" or source_path == destination_path:
        return

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)
    current_path = ""
    for directory_name in destination_dir.split("/"):
        if not directory_name:
            continue
        current_path = os.path.join(current_path, directory_name)
        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass

    with (
        open(source_path, "r") as source_file,
        open(destination_path, "w") as destination_file,
    ):
        destination_file.write(source_file.read())

    os.remove(source_path)
