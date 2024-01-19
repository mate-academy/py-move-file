import os


def move_file(command: str) -> None:
    com_d = command.split()
    if com_d[0] != "mv":
        return None
    n_dir = com_d[2].split("/")
    if len(n_dir) == 1:
        os.rename(com_d[1], com_d[2])
    else:
        dir_path = "/".join(n_dir[:-1]) + "/"
        dir_path = os.path.join(dir_path, os.path.basename(n_dir[-1]))
        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        os.rename(com_d[1], dir_path)
