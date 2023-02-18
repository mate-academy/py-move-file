import os


def move_file(command: str) -> None:
    move_command, from_file, to_file = command.split()
    with open(from_file) as fr_f:
        content = fr_f.read()
    dirs = to_file.split("/")
    final_name = dirs.pop(-1)
    path = ""
    for directory in dirs:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    final_name_path = os.path.join(path, final_name)
    with open(final_name_path, "w") as to_f:
        to_f.write(content)
    os.remove(from_file)
