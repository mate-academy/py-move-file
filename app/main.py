from os import (
    mkdir,
    remove,
    path
)


class MoveCommandSyntaxError(Exception):
    pass


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv":
        raise MoveCommandSyntaxError("Move command not found")

    if len(command) != 3:
        raise MoveCommandSyntaxError(
            "Invalid move command syntax.\n"
            "For a successful moving of file "
            "the command should look like this: "
            "mv file.txt some_dir/new_file.txt"
        )

    file_to_move = command[1]

    if not path.exists(file_to_move):
        raise FileNotFoundError(f"File {file_to_move} does not exist")

    path_of_new_file = command[-1].split("/")
    new_file = path_of_new_file[-1]
    new_file_path = ""

    for part_of_path in path_of_new_file[:-1]:
        new_file_path = path.join(new_file_path, part_of_path)

        try:
            mkdir(new_file_path)
        except FileExistsError:
            pass

    new_file = path.join(new_file_path, new_file)

    with open(file_to_move, "r") as source, open(new_file, "w") as moved:
        moved.write(source.read())

    remove(f"{file_to_move}")
