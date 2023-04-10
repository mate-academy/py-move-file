from os import remove, makedirs


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return
    command, source_path, destination_path = command_split
    if command != "mv":
        return
    destination = destination_path.split("/")
    if len(destination) > 1:
        directory = "/".join(destination[:len(destination) - 1])
        makedirs(directory, exist_ok=True)
    with (open(source_path, "r") as o_file,
          open(destination_path, "w") as c_file
          ):
        c_file.write(o_file.read())
    remove(source_path)
