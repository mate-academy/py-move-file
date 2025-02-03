import os


def move_file(command: str) -> None:
    data = command.split()

    if len(data) != 3 or data[0] != "mv":
        raise ValueError("Uncorrected command")

    source = data[1]
    destination = data[2]

    if not os.path.isfile(source):
        raise FileNotFoundError

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, os.path.basename(source))

    else:
        dir_path = os.path.dirname(destination)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as f:
        file_data = f.read()

    with open(destination, "w") as f:
        f.write(file_data)

    os.remove(source)
