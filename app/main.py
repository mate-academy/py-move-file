from os import rename, path, makedirs, replace


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        raise ValueError("must be: keyword *mv* and two arguments")
    source_line, destination_line = command.split()[1:]
    destination_location, destination_file = path.split(destination_line)
    source_location, source_file = path.split(source_line)
    if path.isfile(source_line) is False or not destination_file:
        raise ValueError("source file is not exist or error in 2nd argument")
    if source_location == destination_location:
        rename(source_line, destination_line)
    else:
        makedirs(destination_location, exist_ok=True)
        if path.isdir(destination_location) is False:
            raise ValueError("can't create directory destination")
        replace(source_line, destination_line)
