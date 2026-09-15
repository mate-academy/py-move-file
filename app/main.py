import os


def move_file(command: str) -> None:
    split_command = command.split()
    _, source, destination = split_command
    if destination.endswith("/") or destination.endswith(os.sep):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with (open(source, "r") as source_file,
          open(destination, "w") as record_file):
        text = source_file.read()
        record_file.write(text)
    os.remove(source)
