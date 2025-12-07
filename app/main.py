import os


def move_file(command: str) -> None:
    _, source_name, destination_name = command.split()

    with open(source_name, "r") as source_file:
        data = source_file.read()

    final_path = destination_name

    if destination_name.endswith("/"):
        os.makedirs(destination_name, exist_ok=True)
        final_path = os.path.join(destination_name, source_name)

    if "/" in destination_name:
        parts = destination_name.split("/")
        file_name = parts[-1]
        path = "/".join(parts[:-1]) + "/"
        os.makedirs(path, exist_ok=True)
        final_path = os.path.join(path, file_name)

    with open(final_path, "w") as destination_file:
        destination_file.write(data)
        os.remove(source_name)
