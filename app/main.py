import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    command_name, first_file, second_file_path = command.split()
    if command_name != "mv" or first_file == second_file_path:
        return

    dir_path = os.path.dirname(second_file_path)
    if dir_path:
        try:
            os.makedirs(dir_path, exist_ok=True)
        except FileExistsError:
            pass

    try:
        with (
            open(first_file, "r")as file_in,
            open(second_file_path, "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(first_file)
    except (FileExistsError, FileNotFoundError):
        return
