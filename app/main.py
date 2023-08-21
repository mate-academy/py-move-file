import os


def move_file(command: str) -> None:
    keyword, source, target = command.strip().split()
    if keyword != "mv":
        return
    if (target_dirname := os.path.dirname(target)) != "":
        os.makedirs(target_dirname, exist_ok=True)
    with open(source, "r") as source_fobj, open(target, "w") as target_fobj:
        target_fobj.write(source_fobj.read())
    os.remove(source)
