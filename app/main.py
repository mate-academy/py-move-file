import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    mv, filename, destination_path = parts
    path, new_filename = os.path.split(destination_path)

    if mv != "mv":
        return

    if path == "":
        os.rename(filename, new_filename)
        return

    dirs = os.path.split(path)
    if "" in dirs:
        dirs = dirs[1:]
    with open(filename, "r") as old_file:
        content = old_file.read()
        previous = ""
        for i, directory in enumerate(dirs):
            directory = os.path.join(previous, directory)
            os.makedirs(directory, exist_ok=True)
            previous = directory

        with open(destination_path, "w") as new_file:
            new_file.write(content)
    os.remove(filename)
