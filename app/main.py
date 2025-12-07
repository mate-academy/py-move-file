import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_name, destination_name = parts

    with open(source_name, "r") as source_file:
        data = source_file.read()

    final_path = destination_name

    if destination_name.endswith("/"):
        os.makedirs(destination_name, exist_ok=True)
        source_basename = os.path.basename(source_name)
        final_path = os.path.join(destination_name, source_basename)

    elif os.path.dirname(destination_name):
        file_name = os.path.basename(destination_name)
        path = os.path.dirname(destination_name)
        os.makedirs(path, exist_ok=True)
        final_path = os.path.join(path, file_name)

    with open(final_path, "w") as destination_file:
        destination_file.write(data)

    os.remove(source_name)
