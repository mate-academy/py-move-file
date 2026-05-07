from pathlib import Path


def move_file(command: str) -> None:
    arguments = command.split()

    if len(arguments) != 3:
        return

    operation, src, dest = arguments
    src_path, dest_path = Path(src), Path(dest)

    if operation != "mv":
        return

    if not src_path.is_file():
        return

    if dest.endswith("/") or dest.endswith("\\"):
        dest_path = dest_path / src_path.name

    dest_dir = dest_path.parent
    dest_dir.mkdir(parents=True, exist_ok=True)

    with open(src_path, "r", encoding="utf-8") as file_in, \
            open(dest_path, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())

    src_path.unlink()
