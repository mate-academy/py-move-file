from pathlib import Path
from shutil import move


def move_file(command: str) -> None:
    input_command, source_path, move_path = command.split()
    if input_command != "mv":
        raise ValueError("The command should be 'mv'")
    elif "/" in move_path:
        path = move_path[:move_path.rfind("/")]
        Path(path).mkdir(parents=True, exist_ok=True)
    move(source_path, move_path)
