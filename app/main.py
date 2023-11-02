import os


def move_file(command: str) -> None:
    mv, source_file, path_file = command.split()
    if len(command.split()) == 3 and mv == "mv":
        if "/" not in path_file:
            os.rename(source_file, path_file)
        elif "/" in path_file:
            full_path_file = path_file
            path_file, new_file_name = os.path.split(path_file)
            if not os.path.exists(path_file):
                os.makedirs(path_file)
            with (
                open(source_file, "r") as in_file,
                open(full_path_file, "w") as out_file
            ):
                out_file.write(in_file.read())

            os.remove(source_file)
