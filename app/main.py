import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        raise ValueError("Invalid command")
    src = command_split[1]
    dst = command_split[2]
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))
    dir_name = os.path.dirname(dst)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(src, "r") as f1, open(dst, "w") as f2:
        file_content = f1.read()
        f2.write(file_content)
    os.remove(src)
