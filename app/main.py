import os
from pathlib import Path


def _ensure_dirs_stepwise(dir_path: str) -> None:
    if not dir_path:
        return

    cur = Path()
    for part in Path(dir_path).parts:
        cur = cur / part
        if not cur.exists():
            os.mkdir(cur)


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, target = parts

    if not (os.path.exists(source) and os.path.isfile(source)):
        return

    if target.endswith("/"):
        target_dir = target.rstrip("/")
        _ensure_dirs_stepwise(target_dir)
        target_path = str(Path(target_dir) / Path(source).name)
    else:
        dir_name = os.path.dirname(target)
        _ensure_dirs_stepwise(dir_name)
        target_path = target

    with open(source, "r") as src, open(target_path, "w") as dst:
        dst.write(src.read())

    os.remove(source)
