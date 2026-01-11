import os


def _normalize(path: str) -> str:
    return path.replace("/", os.path.sep).replace("\\", os.path.sep)


def _ensure_dirs_stepwise(dir_path: str) -> None:
    if not dir_path:
        return

    norm = _normalize(dir_path)
    level = ""
    for part in [p for p in norm.split(os.path.sep) if p]:
        level = os.path.join(level, part) if level else part
        if not os.path.exists(level):
            os.mkdir(level)


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, target = parts

    if not (os.path.exists(source) and os.path.isfile(source)):
        return

    is_dir_target = target.endswith(("/", "\\"))

    if is_dir_target:
        target_dir = _normalize(target.rstrip("/\\"))
        _ensure_dirs_stepwise(target_dir)
        target_path = os.path.join(target_dir, os.path.basename(source))
    else:
        dir_name = _normalize(os.path.dirname(target))
        _ensure_dirs_stepwise(dir_name)
        target_path = _normalize(target)

    with open(source, "r") as src, open(target_path, "w") as dst:
        dst.write(src.read())

    os.remove(source)
