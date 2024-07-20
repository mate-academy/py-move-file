import os
import shlex
import shutil


def move_file(command: str) -> None:
    try:
        command, source_path, destination_path = shlex.split(command)
        if command != "mv":
            raise ValueError("The command is not 'mv'")
    except ValueError as e:
        raise ValueError("The command is not valid") from e

    if source_path == destination_path:
        return

    *source_path, source_file = source_path.split("/")
    full_source_path = os.path.join(*source_path, source_file)

    *destination_path, destination_file = destination_path.split("/")
    destination_file = destination_file or source_file
    if destination_path:
        os.makedirs(os.path.join(*destination_path), exist_ok=True)
        full_destination_path = os.path.join(
            *destination_path, destination_file
        )
    else:
        full_destination_path = destination_file

    shutil.copy2(full_source_path, full_destination_path)
    os.unlink(full_source_path)
