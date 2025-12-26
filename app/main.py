import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    old_file_path = command_parts[1]
    new_file_path = command_parts[2]

    new_path_parts = os.path.split(new_file_path)
    old_path_parts = os.path.split(old_file_path)

    if not new_path_parts[0]:
        os.rename(old_file_path, new_file_path)
        return

    os.makedirs(new_path_parts[0], exist_ok=True)

    new_file_name = new_path_parts[-1]

    path_to_move = new_file_path if new_file_name else (new_file_path
                                                        + old_path_parts[-1])

    with (
        open(old_file_path, "r") as file,
        open(path_to_move, "w") as new_file
    ):
        content = file.read()
        new_file.write(content)

    os.remove(old_file_path)
