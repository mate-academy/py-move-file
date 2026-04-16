import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    if destination.endswith("/"):
        directory = destination
        destination = os.path.join(destination, os.path.basename(source))
    else:
        directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
        os.remove(source)

    except FileNotFoundError:
        pass
