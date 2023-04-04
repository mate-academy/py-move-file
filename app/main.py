import os


def move_file(command: str) -> None:
    arguments = command.split(" ")
    file_to_move = arguments[1]
    new_file_path = None
    if "/" in arguments[2]:
        new_file_path = arguments[2].rpartition("/")[0]
        new_file = arguments[2].rpartition("/")[2]
    else:
        new_file = arguments[2]
    with open(file_to_move, "r") as file_in:
        content = file_in.read()
    os.remove(file_to_move)
    if new_file_path is not None:
        os.makedirs(new_file_path, exist_ok=True)
        with open(arguments[2], "w") as file_out:
            file_out.write(content)
    else:
        with open(new_file, "w") as file_out:
            file_out.write(content)
