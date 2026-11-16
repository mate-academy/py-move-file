import os


def move_file(command: str) -> None:
    parts = command.split()
    old_file = parts[1]
    new_file = parts[2]

    if new_file.endswith("/"):
        new_file += os.path.basename(old_file)

    elements = new_file.split("/")
    path = ""

    for element in elements[:-1]:
        path += f"{element}/"
        if not os.path.exists(path):
            os.mkdir(path)

    if os.path.abspath(old_file) == os.path.abspath(new_file):
        return

    with open(old_file, "rb") as source_file:
        content = source_file.read()

    with open(new_file, "wb") as destination_file:
        destination_file.write(content)

    os.remove(old_file)
