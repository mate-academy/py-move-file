import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "mv":
        return
    source = parts[1]
    destination = parts[2]
    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)
    if os.path.abspath(source) == os.path.abspath(destination):
        return
    directory = os.path.dirname(destination)
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    with open(source, "rb") as file_in, open(destination, "wb") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
