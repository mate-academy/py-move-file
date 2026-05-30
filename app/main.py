import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "mv":
        return

    source_file = parts[1]
    destination_path = parts[2]

    if source_file == destination_path:
        return

    if not os.path.exists(source_file):
        return

    directory = os.path.dirname(destination_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source_file, "r", encoding="utf-8") as file_in, \
            open(destination_path, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
