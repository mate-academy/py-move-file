import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_str, file_name1, file_name2 = parts
    if file_name1 == file_name2 or command_str != "mv":
        return
    dirs = os.path.split(file_name2)
    if not dirs[1]:
        file_name2 += file_name1
    if dirs[0]:
        os.makedirs(dirs[0], exist_ok=True)
    try:
        with (open(file_name1, "r") as source_file,
              open(file_name2, "w") as dest_file):
            for line in source_file:
                dest_file.write(line)
    except FileNotFoundError:
        return
    os.remove(file_name1)
