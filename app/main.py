import shutil
from pathlib import Path


def move_file(command: str) -> None:
    try:
        parts = command.strip().split()
        if len(parts) != 3 or parts[0].lower() != "mv":
            msg = "Invalid command format. Use: \"mv source destination\""
            raise ValueError(msg)

        src = Path(parts[1]).absolute()
        dst = Path(parts[2]).absolute()

        if not src.exists():
            raise FileNotFoundError(f"Source path does not exist: {src}")
        if src.is_dir():
            msg = f"Source is a directory (only files supported): {src}"
            raise IsADirectoryError(msg)

        if (dst.suffix == "" and 
                str(dst).endswith(("\\", "/")) or dst.is_dir()):
            dst = dst / src.name

        if src == dst:
            return

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))

    except (shutil.Error, OSError) as e:
        msg = f"Failed to move {parts[1]} to {parts[2]}: {str(e)}"
        raise OSError(msg) from e


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={
        "test_file": Path("test_file.txt"),
        "test_dir": Path("test_dir")
    })
