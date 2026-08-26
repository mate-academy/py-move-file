import os


def move_file(command: str) -> None:

    command_parts = command.split(" ")
    _, source, destination = command_parts
    if len(command_parts) == 3 and _ == "mv":
        if "/" in destination:
            path, new_file = destination.rsplit("/", 1)
            parts = path.split("/")
            for i in range(len(parts)):
                current_path = os.path.join(*parts[:i + 1])
                if not os.path.exists(current_path):
                    os.mkdir(current_path)
        with open(destination, "w") as f:
            f.write(open(source, "r").read())
        os.remove(source)
