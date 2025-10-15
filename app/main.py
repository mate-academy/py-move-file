import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, target = parts

    if not os.path.exists(source):
        return

    if target.endswith("/"):
        os.makedirs(target, exist_ok=True)
        filename = os.path.basename(source)
        target_path = os.path.join(target, filename)
    else:
        dir_name = os.path.dirname(target)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        target_path = target

    with open(source, "r") as src, open(target_path, "w") as dst:
        dst.write(src.read())

    os.remove(source)
