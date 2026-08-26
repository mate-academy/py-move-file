import os


def move_file(command: str) -> None:

    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "mv":
        _, source, destination = command_parts
        if "/" in destination:
            if destination.endswith("/"):
                destination += os.path.basename(source)
            path, new_file = destination.rsplit("/", 1)
            parts = path.split("/")
            for i in range(len(parts)):
                current_path = os.path.join(*parts[:i + 1])
                if not os.path.exists(current_path):
                    os.mkdir(current_path)
        with open(destination, "w") as f:
            with open(source, "r") as src:
                f.write(src.read())
        os.remove(source)
