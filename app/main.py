import os


def move_file(command: str) -> None:
    operation, file_in, file_to_move = command.split()
    if (
            len(command.split()) != 3
            or operation != "mv"
            or not os.path.isfile(file_in)
            or file_to_move.endswith("/")
    ):
        raise ValueError("The input command has wrong structure")
    if not os.path.exists(file_to_move):
        try:
            os.rename(file_in, file_to_move)
        except FileNotFoundError:
            path, new_file = os.path.split(file_to_move)
            os.makedirs(path, exist_ok=True)
            with (
                open(file_to_move, "w") as created_file,
                open(file_in, "r") as context
            ):
                created_file.write(context.read())
            os.remove(file_in)
