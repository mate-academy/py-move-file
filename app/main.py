from os import makedirs, remove
from os.path import dirname


def move_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return
    com, original_filename, copy_filename = arguments
    if com == "mv" and original_filename != copy_filename:
        if directories := dirname(copy_filename):
            makedirs(directories, exist_ok=True)

        with (open(original_filename, "r") as original_file,
              open(copy_filename, "w") as copy_file):
            copy_file.write(original_file.read())
        remove(original_filename)
