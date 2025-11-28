import os


def move_file(command: str) -> None:
    command_parts = command.split()
    file_to_move = command_parts[1]
    destination = command_parts[2]

    destination = [d for d in destination.split("/") if d]
    path = ""
    new_file = ""

    if "." in destination[-1]:
        new_file = destination[-1]
        for directory in destination[:-1]:
            path += directory + "/"
            os.makedirs(path, exist_ok=True)

    all_path = path + new_file

    with open(file_to_move, "r") as file, open(all_path, "w") as res_file:
        res_file.write(file.read())

    os.remove(file_to_move)
