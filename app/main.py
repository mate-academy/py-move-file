from pathlib import Path
from shutil import move


def move_file(command: str) -> None:
    com_to_execute, old_name, destination = command.split(" ")

    if com_to_execute != "mv":
        raise ValueError("The command should be 'mv'")

    if "/" in destination:
        path = destination[:destination.rfind("/")]
        Path(path).mkdir(parents=True, exist_ok=True)
    move(old_name, destination)
