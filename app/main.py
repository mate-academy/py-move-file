import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        start_command, origin_file, new_file = command
        if start_command == "mv" and "/" not in new_file:
            os.rename(origin_file, new_file)
        if start_command == "mv" and "/" in new_file:
            first_part, second_part = os.path.split(new_file)
            os.makedirs(first_part, exist_ok=True)
            with (open(origin_file, "r") as file_from,
                  open(new_file, "w") as file_to):
                file_to.write(file_from.read())
            os.remove(file_from.name)
