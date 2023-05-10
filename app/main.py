import os


def move_file(command: str) -> None:
    if "mv" in command:
        cmd, origin_file, path = command.split()
        if "/" in path:
            folders, file = os.path.split(path)
            os.makedirs(folders, exist_ok=True)
            with open(origin_file, "r") as f, open(path, "w") as b:
                data = f.read()
                b.write(data)
            os.remove(origin_file)
        else:
            os.rename(origin_file, path)
