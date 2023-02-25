import os


def move_file(command: str) -> None:
    move_command, from_file, to_file = command.split()
    if move_command != "mv":
        raise SyntaxError("No such command")
    dirs = to_file.split("/")
    final_name = dirs.pop(-1)
    path = ""
    for i in dirs:
        path = os.path.join(path, i)
        if not os.path.exists(path):
            os.mkdir(path)
    final_name_path = os.path.join(path, final_name)
    with open(from_file) as fr_f, open(final_name_path, "w") as to_f:
        content = fr_f.read()
        to_f.write(content)
    os.remove(from_file)
