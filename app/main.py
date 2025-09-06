from pathlib import Path


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError()

    func, source, target = parts

    source_path = Path(source)
    if target.endswith("/"):
        target += source_path.name
    target_path = Path(target)

    if source_path.parent == target_path.parent:
        source_path.rename(target_path)
        return

    with open(source, "r") as f:
        content = f.read()

    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        f.write(content)

    source_path.unlink()
