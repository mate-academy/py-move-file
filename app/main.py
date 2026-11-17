import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    if parts[1].startswith("-") or parts[2].startswith("-"):
        return
    action, old_file, new_file = parts

    if new_file.endswith("/"):
        new_file += os.path.basename(old_file)

    elements = new_file.split("/")
    path = ""

    for element in elements[:-1]:
        path = os.path.join(path, element)
        if not os.path.exists(path):
            os.mkdir(path)

    if os.path.abspath(old_file) == os.path.abspath(new_file):
        return

    with open(old_file, "rb") as source_file:
        content = source_file.read()

    with open(new_file, "wb") as destination_file:
        destination_file.write(content)

    os.remove(old_file)
