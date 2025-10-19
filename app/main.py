import os


def move_file(command: str) -> None:
    parts = command.strip().split(maxsplit=2)
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_file, target_path = parts
    if not os.path.isfile(source_file):
        return

    if target_path[-1] in ("/", "\\"):
        target_path = os.path.join(target_path, os.path.basename(source_file))

    directory = os.path.dirname(target_path)
    if directory and not os.path.exists(directory):
        path_part = ""
        for folder in os.path.normpath(directory).split(os.path.sep):
            path_part = os.path.join(path_part, folder)
            if not os.path.exists(path_part) and folder != "":
                os.mkdir(path_part)

    with open(source_file, "r") as file_in, open(target_path, "w") as file_out:
        for line in file_in:
            file_out.write(line)
    os.remove(source_file)
