import os


def move_file(command: str) -> None | str:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return "Invalid command"

    _, source, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with (
        open(source, "r") as orig_file,
        open(destination, "w") as copied_file
    ):
        copied_file.write(orig_file.read())
    os.remove(source)
