import os


def move_file(command: str) -> None:
    try:
        keyword, source, target = command.strip().split()
    except ValueError as e:
        print(f"Invalid command: {e}")
        return
    if keyword != "mv":
        return
    if (target_dirname := os.path.dirname(target)) != "":
        os.makedirs(target_dirname, exist_ok=True)
    with open(source, "r") as source_fobj, open(target, "w") as target_fobj:
        target_fobj.write(source_fobj.read())
    os.remove(source)
