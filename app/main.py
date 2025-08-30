import os.path


def move_file(command: str) -> None:

    command_list = command.split()
    if command_list[0] != "mv":
        return
    if len(command_list) != 3:
        return

    origin_file = command_list[1]
    moving_file = command_list[2]
    if os.path.dirname(moving_file) != "":
        os.makedirs(os.path.dirname(moving_file), exist_ok=True)
    with (open(origin_file) as file_or,
          open(f"{moving_file}", "w") as file_mv):
        file_mv.write(file_or.read())
    os.remove(origin_file)
