import os


def move_file(command: str) -> None:
    com, source, destination = command.split()

    if com != "mv":
        return

    path_to_move = destination.split("/")

    if len(path_to_move) == 1:
        if os.path.exists(destination):
            os.remove(destination)
        os.rename(source, destination)
        return

    path_to_move = "/".join(path_to_move[:-1])

    os.makedirs(path_to_move, exist_ok=True)

    with (open(source, "r") as file_out,
          open(destination, "w") as file_in):
        file_in.write(file_out.read())

    os.remove(source)
