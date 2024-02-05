import os


def move_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        command, original_file, full_path = command.split()
        if "/" in full_path:
            dir_path, new_file_name = os.path.split(full_path)
            if dir_path.endswith("/"):
                dir_path = dir_path[:-1]
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
        if command == "mv" and original_file != full_path:
            with (open(original_file, "r") as origin,
                    open(full_path, "w") as new_file):
                new_file.write(origin.read())
            os.remove(original_file)
