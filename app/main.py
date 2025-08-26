import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "mv":
        start_file, end_file = command_parts[1], command_parts[2]

        dir_path = os.path.dirname(end_file)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(start_file, "r") as file_in, open(end_file, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(start_file)
