import shlex
import os


def move_file(command: str) -> None:
    if command[:3] != "mv ":
        raise ValueError(
            "Expected 'mv' as the first argument"
        )

    source_path, destination_path, *extra_path = shlex.split(command[3:])
    destination_dir, destination_file = os.path.split(destination_path)

    if extra_path:
        raise ValueError(
            "Expected 2 arguements"
        )

    if not os.path.exists(source_path):
        raise FileExistsError(f"File {source_path} not exists")

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with (
        open(source_path, "r") as source_file,
        open(destination_path, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_path)
