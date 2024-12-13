import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "mv":
        source = command_parts[1]
        destination = command_parts[2]

        if destination.endswith("/"):
            os.makedirs(destination, exist_ok=True)
            destination = os.path.join(destination, os.path.basename(source))
        else:
            dir_path = os.path.dirname(destination)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)

        with open(source, "rb") as src_file:
            content = src_file.read()
        with open(destination, "wb") as dest_file:
            dest_file.write(content)

        os.remove(source)
