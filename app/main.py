import os


def move_file(command: str) -> None:
    if not command:
        return

    parts = command.split()
    if len(parts) != 3:
        return

    action, source_path, destination = parts
    if action != "mv":
        return

    if destination.endswith("/"):
        final_path = os.path.join(destination, source_path)
    else:
        final_path = destination

    dir_path = os.path.dirname(final_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(final_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
