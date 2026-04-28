import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return None

    action, source, target = parts

    if action != "mv":
        return None

    if target.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(target, filename)
    else:
        destination = target

    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as f:
        content = f.read()

    with open(destination, "w") as g:
        g.write(content)
    os.remove(source)
