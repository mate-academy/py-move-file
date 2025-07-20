import os


def move_file(command: str) -> None:
    command_parts = command.strip().split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return
    source_file, new_file = command_parts[1], command_parts[2]
    if new_file.endswith("/"):
        new_file = os.path.join(new_file, os.path.basename(source_file))
    new_dirs = os.path.dirname(new_file)
    if new_dirs:
        new_path = ""
        for directory in new_dirs.split(os.sep if os.sep in new_dirs else "/"):
            if not directory:
                continue
            new_path = os.path.join(new_path, directory) if (
                new_path) else directory
            if os.path.exists(new_path):
                if not os.path.isdir(new_path):
                    raise FileExistsError(f"{new_path} exists "
                                          f"and is not a directory!")
            else:
                os.mkdir(new_path)
    try:
        with (open(source_file, "r") as origin_file,
                open(new_file, "w") as moved_file):
            moved_file.write(origin_file.read())
    except FileNotFoundError as e:
        print(e)
        return
    os.remove(source_file)
