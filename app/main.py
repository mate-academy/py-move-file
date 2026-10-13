import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = destination + file_name

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r", encoding="utf-8") as f_in:
        content = f_in.read()

    with open(destination, "w", encoding="utf-8") as f_out:
        f_out.write(content)

    os.remove(source)
