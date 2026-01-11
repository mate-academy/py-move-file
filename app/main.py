import os


def move_file(command: str) -> None:
    parts = command.split()
    action, source_file, path = parts
    if len(parts) == 3 and action == "mv":
        dirs, filename = os.path.split(path)
        if dirs:
            os.makedirs(dirs)
            with (open(source_file, "r") as source,
                  open(path, "w") as new):
                new.write(source.read())
            os.remove(source_file)
        else:
            os.rename(source_file, path)
