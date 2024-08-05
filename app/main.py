import os


def move_file(command: str) -> None:

    if not command.startswith("mv "):
        raise ValueError("Command must start with 'mv '")

    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Use: mv source_file destination_path")

    source_file, destination_path = parts[1], parts[2]

    if source_file == destination_path:
        return

    if destination_path.endswith("/"):
        raise ValueError("Destination path cannot end with a '/' ")

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with (open(source_file, "r") as file_in,
          open(destination_path, "w") as file_out):
        file_out.write(file_in.read())

    os.remove(source_file)
