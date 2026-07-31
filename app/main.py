from os import path as os_path, getcwd, makedirs, remove


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) < 3:
        return

    cm, current_file, path = commands

    if cm != "mv":
        return

    last_slash_index = path.rfind("/")
    is_index = last_slash_index >= 0
    current_path = path.split("/") if is_index else [path]

    if is_index:
        makedirs(path[:last_slash_index], exist_ok=True)

    try:
        with (
            open(current_file, "r") as file,
            open(os_path.join(getcwd(), *current_path), "w") as new_file,
        ):
            new_file.write(file.read())
    except FileNotFoundError:
        print("File not found.", current_file)
    else:
        remove(os_path.join(getcwd(), current_file))
