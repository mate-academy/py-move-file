import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(
            destination, os.path.basename(source)
        )

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as f_in:
        content = f_in.read()

    with open(destination, "w") as f_out:
        f_out.write(content)

    os.remove(source)
