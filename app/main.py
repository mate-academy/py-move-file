import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "mv":
        raise Exception("Wrong command")
    path_to_file = command[2].split("/")

    for num_dir in range(1, len(path_to_file)):
        if os.path.exists("/".join(path_to_file[:num_dir])):
            pass
        else:
            os.mkdir("/".join(path_to_file[:num_dir]))

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        file_out.write(file_in.read())
    os.remove(command[1])
