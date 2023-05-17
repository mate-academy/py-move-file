from os import makedirs, path, remove


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command.split()) != 3 or command_list[0] != "mv":
        raise Exception("Wrong command!")
    mv, incoming_file, new_file = command_list
    dir_path, file_name = path.split(new_file)
    if dir_path:
        makedirs(dir_path, exist_ok=True)
    with (
        open(incoming_file, "r") as incoming,
        open(new_file, "w") as new
    ):
        new.write(incoming.read())
    remove(incoming_file)
