import os


def move_file(command: str) -> None:
    separate_cmd = command.split()
    if len(separate_cmd) == 3:
        cmd, current_file, path_dir = separate_cmd
        if cmd == "mv" and current_file != path_dir:
            dirs, file_name = os.path.split(path_dir)
            if dirs:
                os.makedirs(dirs, exist_ok=True)
            with open(path_dir, "w") as file, \
                    open(current_file, "r") as cur_file:
                file.write(cur_file.read())
            os.remove(current_file)
