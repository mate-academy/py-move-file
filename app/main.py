import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_, file_to_move, path_to_move = command.split()
        if command_ == "mv" and file_to_move != path_to_move.split("/")[-1]:
            place_to_move = path_to_move.split("/")[:-1]
            initial_dir = os.getcwd()
            for folder in place_to_move:    # Creating folder/folders
                os.mkdir(folder)
                os.chdir(f"{os.getcwd()}\\{folder}")
            os.chdir(initial_dir)   # return to original directory
            with (open(file_to_move, "r") as file_in,
                  open(os.path.join(path_to_move), "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_to_move)
