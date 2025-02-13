import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3 or command_list[0] != "mv":
        raise ValueError("Invalid command format")

    source_file = command_list[1]
    target_path = command_list[2]

    directory = os.path.dirname(target_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with (open(source_file, "r") as origin_file,
          open(target_path, "w") as new_file):
        new_file.write(origin_file.read())
        os.remove(source_file)
