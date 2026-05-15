import os


def move_file(command: str) -> None:
    try:
        cmd, old_path, new_path = command.split()
    except ValueError:
        print("Invalid command format. Expected: 'mv <filename> <directory>'")
        return

    if cmd != "mv":
        return

    if new_path.endswith("/") or new_path.endswith(os.sep):
        filename = os.path.basename(old_path)
        new_path = os.path.join(new_path, filename)

    new_directory = os.path.dirname(new_path)
    if new_directory and not os.path.isdir(new_directory):
        os.makedirs(new_directory, exist_ok=True)

    with open(old_path, "r") as orig, open(new_path, "w") as copy:
        copy.write(orig.read())
    os.remove(old_path)
