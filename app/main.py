import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "mv":
        return
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        destination = os.path.join(destination, file_name)
    directory = os.path.dirname(destination)

    if directory:
        parts_of_path = directory.split(os.path.sep)
        current_path = ""
        for part in parts_of_path:
            if not part:
                continue
            if current_path:
                current_path = os.path.join(current_path, part)
            else:
                current_path = part

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as s:
        text = s.read()

    with open(destination, "w") as d:
        d.write(text)

    os.remove(source)











