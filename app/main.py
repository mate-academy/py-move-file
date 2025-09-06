from pathlib import Path


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError()

    command_name, source, destination = parts

    source_path = Path(source)
    if destination.endswith("/"):
        destination += source_path.name
    destination_path = Path(destination)

    if source_path.parent == destination_path.parent:
        source_path.rename(destination_path)
        return

    with open(source, "r") as f:
        content = f.read()

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    with open(destination_path, "w") as f:
        f.write(content)

    source_path.unlink()
