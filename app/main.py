import os
from pathlib import Path


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        raise ValueError("The command should have 3 parts.")
    cmd, source_file, result_file = split_command
    flag = cmd == "mv" and Path(source_file).exists()

    if "/" in result_file:
        result_dir, result_filename = os.path.split(result_file)

        if not result_filename:
            result_filename = Path(source_file).name

        os.makedirs(result_dir, exist_ok=True)

        path_to_result = os.path.join(result_dir, result_filename)
    else:
        path_to_result = Path(result_file).resolve()

    if flag:
        with open(source_file, "r") as source, open(
            path_to_result, "w"
        ) as res:
            source_file_data = source.read()
            res.write(source_file_data)
        Path(source_file).unlink()
