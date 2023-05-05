import os


def move_file(command: str) -> None:
    command_list = command.split()
    if "mv" in command_list and len(command_list) == 3:
        type_command, file_need_to_move, new_file_with_path = command_list
        new_path, new_file = os.path.split(new_file_with_path)
        if new_path:
            os.makedirs(new_path, exist_ok=True)
        with (
            open(file_need_to_move, "r") as file_1,
            open(new_file_with_path, "w") as file_2
        ):
            file_2.write(file_1.read())
        os.remove(file_need_to_move)
