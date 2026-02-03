from pathlib import Path


def move_file(command: str) -> str | None:
    command_parts = command.split(" ")
    if len(command_parts) != 3:
        raise ValueError(
            "Command should be in the format 'mv source destination'"
        )

    source_path = Path(command_parts[1])
    destination_path = Path(command_parts[2])

    if destination_path.is_dir() or destination_path.name.endswith("/"):
        destination_path = destination_path / source_path.name

    destination_path.parent.mkdir(parents=True, exist_ok=True)

    if destination_path == source_path:
        return "The source and destination are the same file."

    if not source_path.exists():
        raise FileNotFoundError

    source_path.rename(destination_path)
