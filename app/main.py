import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Command must to have 3 parts.")

    operation, file1, path_and_file2 = command.split()

    path = os.path.dirname(path_and_file2)
    if path:
        os.makedirs(path, exist_ok=True)
        file_name = path + "/" + path_and_file2.split("/")[-1]
    else:
        file_name = path_and_file2

    with (
        open(file1, "r") as source,
        open(file_name, "w") as new_file
    ):
        new_file.write(source.read())

    os.remove(file1)
