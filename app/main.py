import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        raise ValueError("Command should start with 'mv'")

    _, source, destination = command.split()

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, source.split("/")[-1])
    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with (open(source, "r") as source_file,
          open(destination, "w") as dest_file):
        dest_file.write(source_file.read())
    os.remove(source)
