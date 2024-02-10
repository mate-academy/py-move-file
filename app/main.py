import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    old_file_path = command_parts[1]
    new_file_path = command_parts[2]

    new_path_parts = os.path.split(new_file_path)

    if not new_path_parts[0]:
        os.rename(old_file_path, new_file_path)
        return

    os.makedirs(new_path_parts[0], exist_ok=True)

    with open(old_file_path, "r") as file:
        content = file.read()

    path_to_move = new_file_path

    with open(path_to_move, "w") as new_file:
        new_file.write(content)

    os.remove(old_file_path)
