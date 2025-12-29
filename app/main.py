import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) != 3 or split_command[0] != "mv":
        raise ValueError("Invalid command")

    [source, destination] = split_command[1:]

    if source == destination:
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
        
    dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as src, open(destination, "w") as target:
        target.write(src.read())

    os.remove(source)
