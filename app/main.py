import os


def move_file(command: str) -> None:

    try:
        operation, file_old, file_new = command.split()
    except ValueError:
        return

    if operation != "mv":
        return

    if file_new.endswith("/"):
        file_new = os.path.join(file_new, os.path.basename(file_old))

    path = ""

    for dir_name in file_new.split("/")[:-1]:
        path = os.path.join(path, dir_name)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    with (
        open(os.path.join(
            os.path.dirname(file_old),
            os.path.basename(file_old)),
            "r"
        ) as old_file,
        open(os.path.join(
            path,
            os.path.basename(file_new)),
            "w"
        ) as new_file
    ):
        new_file.write(old_file.read())

    os.remove(file_old)
