import os


def move_file(command: str):
    mv, source_file, path_file = command.split()
    if mv == "mv" and len(command.split()) == 3:
        if "/" not in path_file:
            os.rename(source_file, path_file)
        elif "/" in path_file:
            full_path_file = path_file
            path_file = path_file.split("/")
            new_file_name = path_file[-1]
            path_file.pop(-1)
            path_file = "/".join(path_file)
            if not os.path.exists(path_file):
                os.makedirs(path_file)
            if os.path.exists(new_file_name):
                os.remove(new_file_name)
            with open(source_file, "r") as in_file, open(full_path_file, "w") as out_file:
                out_file.write(in_file.read())

            os.remove(source_file)
