import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    command, initial_file_path, result_file_path = command.split()

    if command != "mv" or initial_file_path == result_file_path:
        return

    os.makedirs(
        os.path.dirname(os.path.abspath(result_file_path)),
        exist_ok=True
    )

    with (
        open(initial_file_path, "r") as initial_file,
        open(result_file_path, "w") as result_file
    ):
        result_file.write(initial_file.read())
    os.remove(initial_file_path)
