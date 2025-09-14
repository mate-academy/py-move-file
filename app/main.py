import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        cmd, source, dest = parts
    else:
        return

    if cmd != "mv" or dest == source or not os.path.isfile(source):
        return

    if dest.endswith(("/", "\\")):
        dest = os.path.join(dest, os.path.basename(source))

    way = os.path.dirname(dest)
    if not os.path.dirname(source) and not way:
        os.rename(source, dest)
    elif way:
        for level in way.split(os.sep):
            if not os.path.isdir(level):
                os.mkdir(level)
        os.replace(source, dest)

    os.remove(source)
