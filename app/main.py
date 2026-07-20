import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format."
                         " Expected: mv source destination")
    mv, source, destination = parts

    new_destination = destination.split("/")
    if destination.endswith("/"):
        dirs = new_destination[:-1]
        filename = source.split("/")[-1]
    else:
        dirs = new_destination[:-1]
        filename = new_destination[-1]

    current_path = ""
    for directory in dirs:
        current_path = os.path.join(current_path, directory)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    full_destination = os.path.join(current_path, filename)

    with open(source) as f:
        content = f.read()

    with open(full_destination, "w") as f:
        f.write(content)

    os.remove(source)
