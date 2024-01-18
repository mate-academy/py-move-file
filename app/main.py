import os


def move_file(command: str) -> None:
    operation, source_file, new_file = command.split()
    if operation == "mv":
        dirs = os.path.dirname(new_file)
        if dirs:
            os.makedirs(dirs, exist_ok=True)

        with (open(source_file, "r") as source,
              open(new_file, "w") as target):
            target.writelines(source.read())
        os.remove(source_file)
