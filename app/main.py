from os import mkdir, remove
from os.path import exists


def move_file(command: str) -> None:
    arguments = command.split(" ")
    if (len(arguments) != 3
            or arguments[0] != "mv"
            or arguments[1] == arguments[2]):
        return

    directories_to_create = arguments[2].split("/")[:-1]
    created = ""
    for directory in directories_to_create:
        created += directory + "/"
        if not exists(created):
            mkdir(created)

    with (open(arguments[1], "r") as original_file,
          open(arguments[2], "w") as copy_file):
        copy_file.write(original_file.read())
    remove(arguments[1])
