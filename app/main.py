import os


def move_file(command: str) -> None:
    source_path, dest_path = command.split()[1:]
    if "/" not in dest_path:
        os.rename(source_path, dest_path)
    elif "/" in dest_path:
        dir_names = []
        for name in dest_path.split("/")[:-1]:
            dir_names.append(name)
            if not os.path.exists("/".join(dir_names)):
                os.mkdir("/".join(dir_names))
        os.rename(source_path, dest_path)
