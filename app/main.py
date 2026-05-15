import os


def move_file(command: str) -> None:
    try:
        cmd, old_path, new_path = command.split()
    except ValueError:
        print("Invalid command format. Expected: 'mv <filename> <directory>'")
        return

    if cmd != "mv":
        return

    new_directory = "/".join(new_path.split("/")[:-1])
    if new_directory and not os.path.isdir(new_directory):
        os.makedirs(new_directory, exist_ok=True)

    with open(old_path, "r") as orig, open(new_path, "w") as copy:
        copy.write(orig.read())
    os.remove(old_path)
