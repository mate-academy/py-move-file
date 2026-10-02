import os


def move_file(command: str) -> None:

    words = command.split()

    if len(words) != 3:
        return
    if words[0] != "mv":
        return

    _, src_file, destination = words

    if destination.endswith("/"):
        directory = destination.rstrip("/")
        destination = os.path.join(directory, os.path.basename(src_file))

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with (open(src_file, "r") as file_in,
              open(destination, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(src_file)
    except FileNotFoundError:
        return
