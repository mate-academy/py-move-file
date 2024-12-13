import os


def move_file(command: str) -> None:
    try:
        operation, file_in, file_to_move = command.split()
    except ValueError as error:
        print(error)
        return
    try:
        if (
            operation != "mv"
            or not os.path.isfile(file_in)
            or file_to_move.endswith("/")
        ):
            raise ValueError("The input command has wrong structure")
    except ValueError as error:
        print(error)
        return
    if not os.path.exists(file_to_move):
        try:
            os.rename(file_in, file_to_move)
        except FileNotFoundError:
            directories, new_file_name = os.path.split(file_to_move)
            os.makedirs(directories, exist_ok=True)
            with (
                open(file_to_move, "w") as created_file,
                open(file_in, "r") as context
            ):
                created_file.write(context.read())
            os.remove(file_in)
