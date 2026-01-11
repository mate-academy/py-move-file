import os


def move_file(command: str) -> None:
    old_path = command.split()[1]
    new_path = command.split()[2]
    if "/" not in new_path:
        os.rename(old_path, new_path)
    else:
        path = new_path.split('/')
        os.makedirs("/".join(path[:-1]))
        with open(old_path, "r") as file_in, \
                open(new_path, "w") as file_out:
            for line in file_in.read():
                file_out.write(line)
    os.remove(old_path)
