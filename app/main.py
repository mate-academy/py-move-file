import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_, file_to_move, path_to_move = command.split()
        path, final_file = os.path.split(path_to_move)
        if command_ == "mv" and file_to_move != final_file:
            os.makedirs(path, exist_ok=True)
            with (open(file_to_move, "r") as file_in,
                  open(os.path.join(path_to_move), "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_to_move)
