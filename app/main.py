import os


def move_file(command: str) -> None:
    command_splitted = command.split()
    cmd = command_splitted[0]
    old_path = command_splitted[1]
    new_path = "/".join(command_splitted[2].split("/")[:-1])
    new_file_name = command_splitted[2].split("/")[-1]

    if cmd != "mv" or old_path == new_path:
        return

    with open(old_path, "r") as source_file:
        data = source_file.read()
        os.makedirs(new_path)
        with open(new_path + "/" + new_file_name, "w") as destination_file:
            destination_file.write(data)
    os.remove(old_path)
