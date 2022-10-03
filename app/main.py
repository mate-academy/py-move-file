import os


def move_file(command: str) -> None:
    command = command.split()
    cmd = command[0]
    old_path = command[1]
    new_path = "/".join(command[2].split("/")[:-1])
    new_file_name = command[2].split("/")[-1]

    if cmd != "mv" or old_path == new_path:
        return print("Wrong data")

    with open(old_path, "r") as source_file:
        data = source_file.read()
        os.makedirs(new_path)
        with open(new_path + "/" + new_file_name, "w") as destination_file:
            destination_file.write(data)
    os.remove(old_path)
