import os


def move_file(command: str) -> None:
    try:
        cmd, source, target = command.split()
    except ValueError:
        return

    if cmd != "mv":
        return

    if target[-1] == "/":
        target = os.path.join(*target.split("/"),
                              os.path.basename(source))

    path = ""
    if len(target.split("/")) > 1:
        path = os.path.join(*target.split("/")[:-1])

    if path and not os.path.exists(path):
        os.makedirs(path)

    with (open(source, "r") as source_file,
          open(f"{target}", "w") as target_file):
        target_file.write(source_file.read())

    os.remove(source)
