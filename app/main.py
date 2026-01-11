import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cmd, source, destination = parts
    if cmd != "mv":
        return

    if not os.path.isfile(source):
        return

    if destination.endswith("/") or destination.endswith("\\"):
        dst_path = os.path.join(destination, os.path.basename(source))
    else:
        dst_path = destination

    dir_to_create = os.path.dirname(dst_path)
    if dir_to_create:
        os.makedirs(dir_to_create, exist_ok=True)

    with open(source, "rb") as fsrc, open(dst_path, "wb") as fdest:
        while chunk := fsrc.read(4096):
            fdest.write(chunk)

    os.remove(source)
