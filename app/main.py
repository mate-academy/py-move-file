import os


def move_file(command: str) -> None:
    try:
        cmnd, file_name, new_path = command.split(" ")
        if cmnd == "mv":
            new_path_dir = os.path.dirname(new_path)
            if new_path_dir:
                if not os.path.exists(new_path_dir):
                    os.makedirs(new_path_dir)
            os.rename(file_name, new_path)
    except ValueError:
        pass
