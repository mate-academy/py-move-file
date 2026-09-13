import os


def move_file(command: str) -> None:
    command = command.split()
    source = command[1]
    destination = command[2]
    if destination.endswith("/"):
        folder = destination
        filename = source
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
