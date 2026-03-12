import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "mv":
        _, source, destination = parts

        if destination.endswith("/"):
            destination = os.path.join(destination, os.path.basename(source))

        directory_path = os.path.dirname(destination)
        if directory_path:
            os.makedirs(directory_path, exist_ok=True)

        if os.path.exists(source):
            with open(source, "r") as src_file:
                content = src_file.read()

            with open(destination, "w") as dst_file:
                dst_file.write(content)

            os.remove(source)
