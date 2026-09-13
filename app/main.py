import os


def move_file(command: str) -> None:
    tokens = command.split()

    if len(tokens) != 3 or tokens[0] != "mv":
        raise ValueError("Command must be in format: mv <source> <destination>")

    action, source, destination = tokens

    if destination.endswith("/"):
        folder = destination
        filename = os.path.basename(source)
    else:
        folder, filename = os.path.split(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(source, "r") as old_file:
        content = old_file.read()

    new_path = os.path.join(folder, filename)

    with open(new_path, "w") as new_file:
        new_file.write(content)

    os.remove(source)