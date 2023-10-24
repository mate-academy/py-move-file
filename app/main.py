import os


def move_file(command: str) -> None:
    cm, name_file, directory = command.split()
    if cm != "mv" or name_file == directory or directory == "":
        return
    new_dir = os.path.dirname(directory)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    with open(name_file, "r") as old_file, open(directory, "w") as new_file:
        new_file.write(old_file.read())
    os.remove(name_file)
