import os


def move_file(command: str) -> None:
    cmd_parts = command.split()
    if len(cmd_parts) != 3 or cmd_parts[0] != "mv":
        raise ValueError("Invalid command format")
    cmd, source_file, destination_file = cmd_parts

    if destination_file.endswith(("/", os.sep)):
        destination_file = os.path.join(destination_file,
                                        os.path.basename(source_file))

    dest_dir = os.path.dirname(destination_file)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    with open(source_file, "r") as src:
        with open(destination_file, "w") as dst:
            dst.write(src.read())

    os.remove(source_file)
