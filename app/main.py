import os


def move_file(command: str) -> None:
    comm, file_to_move, path_to_move = command.split()
    place_to_move = path_to_move.split("/")[:-1]
    for dir in place_to_move:
        os.mkdir(dir)
        os.chdir(f"{os.getcwd()}\\{dir}")
    os.chdir(f"{'../' * len(place_to_move)}/")
    with (open(file_to_move, "r") as file_in, open(os.path.join(path_to_move), "w") as file2):
        file2.write(file_in.read())
    os.remove(file_to_move)

