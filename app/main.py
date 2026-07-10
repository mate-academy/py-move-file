import os


def move_file(command: str) -> None:
    try:
        cmd, source, target = command.split()
    except ValueError:
        return

    if cmd != "mv":
        return

    if "/" in target:
        target_dir = target.rsplit("/", 1)[0]
        os.makedirs(target_dir, exist_ok=True)

    with (open(source, "r") as source_file,
          open(f"{target}", "w") as target_file):
        target_file.write(source_file.read())

    os.remove(source)
