import os


def move_file(command: str) -> None:
    if not command:
        return
    split_command = command.split()
    if len(split_command) != 3:
        return
    cmd, source_path, dest_path = split_command
    if cmd != "mv":
        return
    if not os.path.dirname(dest_path):
        with (open(source_path, "r") as file_src,
              open(dest_path, "w") as file_dest):
            file_dest.write(file_src.read())
        os.remove(source_path)
        return
    dir_path = os.path.dirname(dest_path)
    parts = dir_path.split(os.sep)
    current_path = ""
    for part in parts:
        if part:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    with (open(source_path, "r") as file_src,
          open(dest_path, "w") as file_dest):
        file_dest.write(file_src.read())
    os.remove(source_path)
