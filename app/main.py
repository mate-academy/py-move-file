import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    _, source, destination = parts

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)

    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r", encoding="utf-8") as f_in:
        content = f_in.read()

    with open(destination, "w", encoding="utf-8") as f_out:
        f_out.write(content)

    os.remove(source)
