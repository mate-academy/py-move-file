from os import rename, path, makedirs, replace


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        raise ValueError("must be: keyword *mv* and two arguments")
    source_path, destination_path = command.split()[1:]
    destination_dirs, destination_filename = path.split(destination_path)
    source_dirs, source_filename = path.split(source_path)
    if path.isfile(source_path) is False or not destination_filename:
        raise ValueError("source file is not exist or error in 2nd argument")
    if source_dirs == destination_dirs:
        rename(source_path, destination_path)
    else:
        makedirs(destination_dirs, exist_ok=True)
        if path.isdir(destination_dirs) is False:
            raise ValueError("can't create directory destination")
        replace(source_path, destination_path)
