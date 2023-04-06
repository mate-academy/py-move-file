from os import remove, makedirs


def move_file(command: str) -> None:
    command_name, origin_file, path_file = command.split()
    if command_name != "mv":
        raise Exception("Wrong command!")
    destination = path_file.split("/")
    if len(destination) > 1:
        directory = "/".join(destination[:len(destination) - 1])
        makedirs(directory, exist_ok=True)
    with (open(origin_file, "r") as o_file,
          open(path_file, "w") as c_file
          ):
        c_file.write(o_file.read())
    remove(origin_file)
