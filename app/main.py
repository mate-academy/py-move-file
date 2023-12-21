import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) == 3 and command_parts[0] == "mv":
        source_file = command_parts[1]
        destination_path = command_parts[2]

        if destination_path.endswith("/"):
            destination_file = os.path.join(
                destination_path, os.path.basename(source_file))
            os.makedirs(destination_path, exist_ok=True)
        else:
            destination_file = destination_path

        dir_name = os.path.dirname(destination_file)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(source_file, "rb") as src, \
                open(destination_file, "wb") as dst:
            dst.write(src.read())
        os.remove(source_file)
