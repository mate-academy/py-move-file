import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    mv, first_file, second_file = (
        split_command[0],
        split_command[1],
        split_command[2])

    if len(split_command) != 3 or mv != "mv":
        return

    if not os.path.exists(first_file):
        return

    if second_file.endswith("/"):
        os.makedirs(second_file, exist_ok=True)
        second_file = os.path.join(second_file, os.path.basename(first_file))
    else:
        dir_path = os.path.dirname(second_file)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
    os.rename(first_file, second_file)
