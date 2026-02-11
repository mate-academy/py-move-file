import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_str, file_name1, file_name2 = parts
    if file_name1 == file_name2 or command_str != "mv":
        return
    dirs = file_name2.split("/")
    dirs.pop(-1)
    for index in range(len(dirs)):
        try:
            os.mkdir("/".join(dirs[:index + 1]))
        except Exception:
            continue
    try:
        with (open(file_name1, "r") as source_file,
              open(file_name2, "w") as dest_file):
            for line in source_file:
                dest_file.write(line)
    except FileNotFoundError:
        return
    os.remove(file_name1)
