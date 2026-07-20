import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must be in the form: mv <source> <destination>")

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        target_path = os.path.join(destination.rstrip("/"), os.path.basename(source))
    else:
        target_path = destination

    parent_directory = os.path.dirname(target_path)
    if parent_directory:
        os.makedirs(parent_directory, exist_ok=True)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(target_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
