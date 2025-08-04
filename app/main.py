import os


def move_file(command: str) -> None:
    parts = command.split()

    action = parts[0]
    source_file_name = parts[1]
    destination = parts[2]

    if len(parts) != 3 or action != "mv":
        return

    if not os.path.isfile(source_file_name):
        return

    dst_for_file = os.path.dirname(destination)

    if dst_for_file:
        os.makedirs(dst_for_file, exist_ok=True)

    if source_file_name == destination:
        return

    try:
        with open(source_file_name, "r") as src_file:
            content = src_file.read()
        with open(destination, "w") as dst_file:
            dst_file.write(content)
    except FileNotFoundError:
        raise FileNotFoundError("File is not")

    os.remove(source_file_name)
