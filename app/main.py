import os


def move_file(command: str) -> None:
    cmd, source, path = command.split()

    if "/" not in path:
        os.rename(source, path)
        return

    dir_path = path.split("/")[:-1]

    os.makedirs("/".join(dir_path), exist_ok=True)
    with open(source, "r") as file_in, open(path, "a") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
