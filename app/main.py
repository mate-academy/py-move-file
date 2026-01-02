import os


def move_file(command: str) -> None:
    cm_list = command.split()

    if "mv" != cm_list[0] or len(cm_list) < 3:
        return

    path_from = cm_list[1]
    path_to = cm_list[2]
    directories = path_to.split("/")[:-1]

    if path_from == path_to:
        return

    if directories:
        current_path = "."
        for directory in directories:
            current_path = os.path.join(current_path, directory)
            os.makedirs(current_path, exist_ok=True)
        try:
            with open(path_from) as file_from, open(path_to, "w") as file_to:
                content = file_from.read()
                file_to.write(content)
            os.remove(path_from)
        except FileNotFoundError as e:
            print(e)
    else:
        os.rename(path_from, path_to)
