import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv source_file destination_path"
        )

    _, source_path, destination_path = parts

    if not os.path.exists(source_path):
        raise FileNotFoundError(
            f"Source file {source_path} does not exist."
        )

    if destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        new_file_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )
    else:
        dir_name = os.path.dirname(destination_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        new_file_path = destination_path

    with open(source_path, "r") as src:
        content = src.read()

    with open(new_file_path, "w") as dst:
        dst.write(content)

    os.remove(source_path)
