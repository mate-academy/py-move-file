import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        return
    first_value, second_value, third_value = command_list
    if first_value != "mv":
        return
    if third_value.endswith("/"):
        os.makedirs(third_value, exist_ok=True)
        third_value = os.path.join(third_value, os.path.basename(second_value))
    else:
        dir_path = os.path.dirname(third_value)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
    os.rename(second_value, third_value)
