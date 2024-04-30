import shlex
import os


def move_file(command: str) -> None:
    command, source_path, destination_path, *extra_path = shlex.split(command)
    destination_dir, destination_file = os.path.split(destination_path)

    validate_mv_data(command, source_path, extra_path)

    if not destination_file:
        if os.path.isfile(source_path):
            destination_path += os.path.splitext(source_path)[-1]

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)
    try:
        with (
            open(source_path, "r") as source_file,
            open(destination_path, "w") as destination_file
        ):
            destination_file.write(source_file.read())
        os.remove(source_path)
    except OSError as e:
        print(f"The command did not work out: {e}")


def validate_mv_data(command: str, source_path: str, extra_path: str) -> None:
    if command != "mv":
        raise ValueError(
            "Expected 'mv' as the first argument"
        )

    if extra_path:
        raise ValueError(
            "Expected 2 arguements"
        )

    if not os.path.exists(source_path):
        raise FileExistsError(f"File {source_path} not exists")
