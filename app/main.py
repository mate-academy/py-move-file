import os


def move_file(command: str) -> None:
    arguments = command.split(" ")
    if len(arguments) != 3:
        return
    operation, src, dest = arguments
    if not os.path.exists(src) or operation != "mv":
        return
    directory = os.path.dirname(dest)
    if directory:
        os.makedirs(directory, exist_ok=True)
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))
    with open(src, "r") as src_file, open(dest, "w") as dest_file:
        dest_file.write(src_file.read())
    os.remove(src)
