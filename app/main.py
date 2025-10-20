import os


def move_file(command: str) -> None:
    tokens = command.strip().split()
    if len(tokens) != 3 or tokens[0] != "mv":
        return

    source, destination = tokens[1], tokens[2]

    if not os.path.isfile(source):
        return

    if os.path.basename(os.path.normpath(destination)) == "":
        destination = os.path.join(destination, os.path.basename(source))

    dst_dir = os.path.dirname(destination)
    if dst_dir:
        os.makedirs(dst_dir, exist_ok=True)

    with open(source, "r") as f_src:
        content = f_src.read()

    with open(destination, "w") as f_dst:
        f_dst.write(content)

    os.remove(source)
