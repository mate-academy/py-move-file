import os


def move_file(command: str) -> None:
    try:
        cmd, source, target = command.split()
    except ValueError:
        return

    if cmd != "mv":
        return

    if "/" in target:
        if target[-1] != "/":
            basename = target.split("/")[-1]
        else:
            basename = source

        target = source.split("/")[:-1]
        path = os.path.join(*target, basename)

        os.makedirs(path)

    with (open(source, "r") as source_file,
          open(f"{target}", "w") as target_file):
        target_file.write(source_file.read())

    os.remove(source)
