from os import makedirs, remove, rename, path


def move_file(command: str) -> None:

    if not command.startswith("mv"):
        return

    com, old_filename, path_and_new_filename = command.split()
    full_path, new_filename = path.split(path_and_new_filename)

    if path_and_new_filename == new_filename:
        rename(old_filename, new_filename)
        return

    makedirs(full_path, exist_ok=True)

    with (open(old_filename, "r") as old_file,
          open(path_and_new_filename, "w") as new_file):
        new_file.write(old_file.read())
    remove(old_filename)
