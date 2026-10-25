import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv" or parts[1] == parts[2]:
        return

    _, source, destination = parts

    try:
        with open(source, "r", encoding="utf-8") as src:
            content = src.read()
    except FileNotFoundError:
        return

    if destination.endswith("/"):
        directories = [dir_name for dir_name
                       in destination.split("/") if dir_name]
        destination_file = os.path.join(*directories, os.path.basename(source))
    elif "/" in destination:
        path_elements = destination.split("/")
        directories = path_elements[:-1]
        destination_file = os.path.join(*path_elements)
    else:
        directories = []
        destination_file = destination

    current_path = ""
    for directory in directories:
        current_path = os.path.join(current_path, directory)
        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass

    with open(destination_file, "w", encoding="utf-8") as dst:
        dst.write(content)

    os.remove(source)
