import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        return

    action, original_file, moved_file_path = split_command
    if original_file == moved_file_path or action != "mv":
        return

    dirpath = os.path.dirname(moved_file_path)
    if dirpath:
        parts = [p for p in dirpath.split("/") if p]
    else:
        parts = []

    acc = []

    for part in parts:
        acc.append(part)
        current_path = os.path.join(*acc)
        if os.path.exists(current_path):
            if os.path.isdir(current_path):
                continue
            else:
                raise FileExistsError

        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass

    try:
        with (open(original_file, "rb") as file_in,
              open(moved_file_path, "wb") as file_out):
            file_out.write(file_in.read())

    except OSError:
        return
    else:
        os.remove(original_file)
