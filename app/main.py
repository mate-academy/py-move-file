import os


def move_file(command: str) -> None:
    commands = command.split()

    if commands[0] != "mv" or len(commands) != 3:
        return None

    mv, source_path, new_path = commands

    if not os.path.exists(source_path):
        return None

    make_dir = os.path.dirname(new_path)

    if make_dir:
        os.makedirs(make_dir, exist_ok=True)

    with (
        open(source_path, "r") as source_file,
        open(new_path, "w") as copy_file
    ):
        copy_file.write(source_file.read())

    os.remove(source_path)
