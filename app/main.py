import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    with open(source_path, "r") as source_file:
        content = source_file.read()

    if destination_path.endswith("/"):
        file_name = os.path.basename(source_path)
        destination_path = destination_path + file_name

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        current_path = ""

        for directory in destination_dir.split("/"):
            if current_path == "":
                current_path = directory
            else:
                current_path = current_path + "/" + directory

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
