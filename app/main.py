from os import makedirs, remove, path, rename


def move_file(command: str) -> None:
    source_data = command.split()
    paths = source_data[2].split("/")
    new_path = "/".join(paths[:-1])
    if "/" in source_data[2]:
        makedirs(new_path)
        with open(source_data[1], "w+") as file_in, \
             open(path.join(new_path, paths[-1]), "w") as file_out:
            save_data = file_in.read()
            file_out.write(save_data)
        remove(source_data[1])
    else:
        try:
            rename(source_data[1], paths[-1])
        except FileNotFoundError:
            raise
