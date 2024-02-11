from os import makedirs, remove
from os.path import join


def move_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return
    com, original_filename, copy_filename = arguments
    if com != "mv" or original_filename == copy_filename:
        return

    new_path = join("", *arguments[2].split("/")[:-1])
    makedirs(new_path, exist_ok=True)

    with (open(original_filename, "r") as original_file,
          open(copy_filename, "w") as copy_file):
        copy_file.write(original_file.read())
    remove(original_filename)
