import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        return

    old_file = parts[1]
    new_file = parts[2]

    path_parts = new_file.split("/")
    if len(path_parts) > 1:
        os.makedirs("/".join(path_parts[:-1]), exist_ok=True)

    with open(old_file, "r") as old, open(new_file, "w") as new:
        content = old.read()
        new.write(content)

    os.remove(old_file)
