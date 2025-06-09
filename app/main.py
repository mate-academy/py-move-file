import os


def move_file(command_file: str) -> None:
    parts = command_file.split()
    if parts[0] != "mv" or len(parts) != 3:
        return
    rsc = parts[1]
    dst = parts[2]
    new_dir = os.path.dirname(dst)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    with open(rsc, "r") as old_file, open(dst, "w") as new_file:
        new_file.write(old_file.read())
    os.remove(rsc)
