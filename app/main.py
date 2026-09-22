import os


def move_file(command: str) -> None:
    try:
        [cmd, file_to_move, place_to_move] = command.split()

        if cmd != "mv":
            raise ValueError
    except ValueError:
        print("Invalid command")
        raise

    parts_of_path = place_to_move.split("/")
    new_file_name = parts_of_path[-1]

    if len(parts_of_path) == 1:
        try:
            with (
                open(file_to_move, "r") as file,
                open(new_file_name, "w") as new_file
            ):
                new_file.write(file.read())
        except (FileNotFoundError, FileExistsError):
            raise

        os.remove(file_to_move)

        return

    base_path = os.getcwd()
    path_to_move = os.path.join(base_path, *parts_of_path[:-1])

    for index in range(0, len(parts_of_path) - 1):
        # first_dir second_dir third_dir
        iteration_path = os.path.join(base_path, parts_of_path[index])

        if not os.path.isdir(iteration_path):
            os.mkdir(iteration_path)

        base_path = iteration_path

    if place_to_move[-1] == "/":
        try:
            with (
                open(file_to_move, "r") as file,
                open(os.path.join(path_to_move, file_to_move), "w") as new_file
            ):
                new_file.write(file.read())
        except (FileNotFoundError, FileExistsError):
            raise

        os.remove(file_to_move)
    else:
        try:
            with (
                open(file_to_move, "r") as file,
                open(os.path.join(
                    path_to_move,
                    new_file_name
                ), "w") as new_file
            ):
                new_file.write(file.read())

            os.remove(file_to_move)
        except (FileNotFoundError, FileExistsError):
            raise
