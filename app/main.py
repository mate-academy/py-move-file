import os


def move_file(command: str):
    tokens = command.split()
    if len(tokens) != 3 or tokens[0] != "mv" :
        return
    _, src_path, dest_path = tokens

    if dest_path.endswith(("/", os.path.sep)):
        dest = os.path.join(dest_path, os.path.basename(src_path))
    else:
        dest = dest_path
    dirs = dest.split("/")[:-1]
    current = ""
    for folder in dirs:
        current += folder + "/"
        if not os.path.exists(current):
            os.mkdir(current)
    with open (src_path, "r") as src_file:
        content = src_file.read()
        with open (dest, "w") as dest_file:
            dest_file.write(content)
    os.remove(src_path)
