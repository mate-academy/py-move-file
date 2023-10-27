import os


def move_file(command: str) -> None:
    if not (len(command.split()) == 3):
        return

    mv, old_filename, new_filepath = command.split()
    path, new_filename = os.path.split(new_filepath)

    if mv != "mv":
        return

    if path == "":
        os.rename(old_filename, new_filename)
        return

    dirs = path.split("/")
    with open(old_filename, "r") as old_file:
        old_file_content = old_file.read()
        previous = ""
        for i, directory in enumerate(dirs):
            directory = os.path.join(previous, directory)
            os.makedirs(directory, exist_ok=True)
            previous = directory

        with open(new_filepath, "w") as new_file:
            new_file.write(old_file_content)
    os.remove(old_filename)
