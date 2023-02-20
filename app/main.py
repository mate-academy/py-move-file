import os


def move_file(command: str) -> None:
    command_parts = command.split()
    file_to_move = command_parts[1]
    if "/" in command_parts[2]:
        directory, new_file = command_parts[2].rsplit("/", 1)
        os.makedirs(directory)
    else:
        os.rename(file_to_move, command_parts[-1])
        return
    with open(file_to_move, "r") as file_from, \
            open(os.path.join(directory, new_file), "w") as file_to:
        file_to.write(file_from.read())
        os.remove(file_to_move)
