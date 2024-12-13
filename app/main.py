import os


def move_file(command: str) -> None:
    split_command = command.split()
    if (
        len(split_command) != 3
        or split_command[0] != "mv"
    ):
        return

    original_file = split_command[1]
    new_file_path = split_command[2]

    if original_file == new_file_path:
        return

    directory, filename = os.path.split(new_file_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with (
        open(original_file, "r") as old_file,
        open(split_command[2], "w") as new_file
    ):
        new_file.write(old_file.read())

    os.remove(original_file)
