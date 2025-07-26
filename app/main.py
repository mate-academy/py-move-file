import os


def move_file(command: str) -> None | str:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format.")

    command, source, destination = parts

    if source == destination:
        return "File already exists at the destination."

    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    with open(source, "r") as source_file:
        text_copy = source_file.read()

    abs_dest_path = os.path.abspath(destination)
    dest_dir = os.path.dirname(abs_dest_path)

    if dest_dir and os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
        raise FileExistsError(
            f"A file named '{dest_dir}' already exists and blocks folder creation."
        )

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(destination, "w") as dest_file:
        dest_file.write(text_copy)

    os.remove(source)
