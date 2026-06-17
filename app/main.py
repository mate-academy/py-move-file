import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "mv":
        return

    _, source_file, destination = parts

    if destination.endswith("/"):
        destination = os.path.join(destination, source_file)

    dirs = destination.split("/")[:-1]

    current_path = ""

    for directory in dirs:
        current_path = os.path.join(current_path, directory)

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source_file, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
