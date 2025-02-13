import os


def move_file(command: str) -> None:
    file_to_delete, file_to_move = command.split(" ")[1:]

    with open(file_to_delete, "r") as file:
        text = file.read()

    path_to_move = "/".join(file_to_move.split("/")[:-1])
    os.remove(file_to_delete)

    if path_to_move != "":
        os.makedirs(path_to_move, exist_ok=True)

    with open(file_to_move, "w") as file:
        file.write(text)
