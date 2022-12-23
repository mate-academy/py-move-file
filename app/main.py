import os


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv":
        raise NameError("The command does not exists")

    file_to_read = command[1]
    list_to_join = command[2].split("/")
    new_dir = "/".join(list_to_join[:-1])
    os.makedirs(new_dir)
    path_to_file = "/".join(list_to_join)

    with (open(file_to_read, "r") as source,
          open(path_to_file, "a") as receiver):
        receiver.write(source.read())
    os.remove(file_to_read)
