import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_, file_to_move, path_to_move = command.split()
        if command_ == "mv":
            place_to_move = path_to_move.split("/")[:-1]
            for direction in place_to_move:
                os.mkdir(direction)
                os.chdir(f"{os.getcwd()}\\{direction}")
            os.chdir(f"{'../' * len(place_to_move)}/")
            with (open(file_to_move, "r") as file_in,
                  open(os.path.join(path_to_move), "w") as file2):
                file2.write(file_in.read())
            os.remove(file_to_move)
