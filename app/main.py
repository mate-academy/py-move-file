import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if parts[0] != "mv" or len(parts) != 3:
        return

    mv, source_file_name, destination_file_name = parts

    if source_file_name == destination_file_name:
        return

    if destination_file_name.endswith('/') or destination_file_name.endswith('\\'):
        source_file_name = os.path.basename(source_file_name)
        destination_file_name = os.path.join(destination_file_name, source_file_name)

    try:
        os.path.join(destination_file_name)
        destination_dir = os.path.dirname(destination_file_name)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

        with (
            open(source_file_name, "r") as file_in,
            open(destination_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())
        os.remove(source_file_name)

    except FileNotFoundError:
        return
