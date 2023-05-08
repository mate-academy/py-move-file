import os


def move_file(command: str) -> None:
    cmd, origin_file, path = command.split()
    if cmd == "mv":
        if "/" in path:
            part_of_path = path.split("/")
            part_of_path.pop()
            new_path = "/".join(part_of_path)
            os.makedirs(new_path, exist_ok=True)
            with open(origin_file, "r") as f:
                date = f.read()
            with open(path, "w") as b:
                b.write(date)
            os.remove(origin_file)
        else:
            os.rename(origin_file, path)
