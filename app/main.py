import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Command must to have 3 parts.")

    operation, source_file, path_and_file2 = command.split()

    if operation != "mv":
        raise ValueError("Operation must be mv.")

    path = os.path.dirname(path_and_file2)
    if path:
        os.makedirs(path, exist_ok=True)

    with (
        open(source_file, "r") as source,
        open(path_and_file2, "w") as new_file
    ):
        new_file.write(source.read())

    os.remove(source_file)
