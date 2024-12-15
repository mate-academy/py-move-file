import os


class MvError(Exception):
    pass


def move_file(command: str) -> None:
    _, source_file, path = command.split()

    if len(command.split()) != 3:
        raise MvError(
            "Invalid command format. "
            "Expected: mv source_file destination_path."
        )

    path_ls = path.split("/")
    current_path = ""

    for i in path_ls[:-1]:
        current_path = os.path.join(current_path, i)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    new_file_path = os.path.join(current_path, path_ls[-1])

    if path.endswith("/"):
        new_file_path = os.path.join(new_file_path, source_file)

    with open(source_file, "r") as file_in, open(new_file_path, "w") as new_fl:
        new_fl.write(file_in.read())

    os.remove(source_file)
