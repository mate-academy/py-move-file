from pathlib import Path


def move_file(command: str) -> None:
    func, source, target = command.split()

    source_path = Path(source)
    target_path = Path(target)

    if source_path.parent == target_path.parent:
        source_path.rename(target_path)
        return

    with open(source, "r") as f:
        content = f.read()

    source_path.unlink()

    target_path.parent.mkdir(parents=True, exist_ok=True)

    with open(target_path, "w") as f:
        f.write(content)
