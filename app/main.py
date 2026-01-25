import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command")

    _, src, dst = parts
    if dst.endswith("/"):
        dst = dst + os.path.basename(src)

    dir_path = os.path.dirname(dst)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)


    with open(src, "r") as source_file:
        content = source_file.read()

    with open(dst, "w") as target_file:
        target_file.write(content)

    os.remove(src)
