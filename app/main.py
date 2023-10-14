import os


def move_file(command: str) -> None:
    mv_command = command.split()
    if len(mv_command) == 3 or mv_command[0] == "mv":
        source_file, destination_path = mv_command[1], mv_command[2]
        path_file = os.path.dirname(destination_path)
        if path_file:
            os.makedirs(path_file, exist_ok=True)
        os.replace(source_file, destination_path)
