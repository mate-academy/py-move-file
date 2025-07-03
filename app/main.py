import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source_path, dest_path = parts

    if not os.path.exists(source_path):
        return

    if dest_path.endswith("/"):
        filename = os.path.basename(source_path)
        dest_path = os.path.join(dest_path, filename)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with (
        open(source_path, "rb") as file_in,
        open(dest_path, "wb") as file_out,
    ):
        file_out.write(file_in.read())
    os.remove(source_path)
