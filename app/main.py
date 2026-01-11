import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Value Error, indicate the path correctly")

    command_list = command.split()
    first_file = command_list[1]
    final_file = command_list[2]

    if command_list[0] != "mv":
        raise ValueError("Command must be mv")

    file_path = os.path.dirname(final_file)

    if file_path:
        os.makedirs(file_path, exist_ok=True)

    os.replace(first_file, final_file)
