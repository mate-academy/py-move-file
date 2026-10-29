import os


def move_file(command: str) -> None:
    split_command: list[str] = command.strip().split()

    if (
        len(split_command) != 3
        or split_command[0] != "mv"
        or split_command[1] == ""
        or split_command[2] == ""
    ):
        return

    _, source_file_name, destination_file_name = split_command

    if destination_file_name.endswith(("/", "\\")):
        make_dirs(destination_file_name)
        destination_file_name = os.path.join(
            destination_file_name,
            os.path.basename(source_file_name)
        )
    else:
        dir_path = os.path.dirname(destination_file_name)

        if dir_path:
            make_dirs(dir_path)

    try:
        with (
            open(source_file_name, "r") as file_in,
            open(destination_file_name, "w") as file_out
        ):
            file_out.write(file_in.read())

    except FileNotFoundError:
        return

    else:
        os.remove(source_file_name)


def make_dirs(path: str) -> None:
    path = path.replace("\\", os.sep).replace("/", os.sep)
    path = os.path.normpath(path)

    current_path = ""

    for part in path.split(os.sep):
        if not part:
            continue

        current_path = os.path.join(current_path, part)

        try:
            os.mkdir(current_path)
        except FileExistsError:
            if not os.path.isdir(current_path):
                raise
