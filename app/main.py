import os
from pathlib import Path


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        raise ValueError("The command should have 3 parts.")
    cmd, source_file, result_file = split_command
    flag = cmd == "mv" and Path(source_file).exists()

    result_dir, result_filename = os.path.split(result_file)

    if not result_filename:
        result_filename = Path(source_file).name

    if result_dir:
        os.makedirs(result_dir, exist_ok=True)

    if flag:
        with open(source_file, "r") as source, open(
            result_file, "w"
        ) as res:
            source_file_data = source.read()
            res.write(source_file_data)
        Path(source_file).unlink()
