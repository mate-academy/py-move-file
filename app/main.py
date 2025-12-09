import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command")
        return

    source = parts[1]
    dest = parts[2]

    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as src, open(dest, "w") as dst:
        dst.write(src.read())

    os.remove(source)
