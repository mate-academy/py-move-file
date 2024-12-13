import os


def move_file(command: str) -> None:
    command_split = command.split()
    command_flag, first_file, second_file = command_split
    if command_flag == "mv" and len(command_split) == 3:
        directory, new_file = os.path.split(second_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        new_directory = os.path.join(directory, new_file)
        with (open(first_file, "r") as recent_file,
              open(new_directory, "w") as upgrade_file):
            upgrade_file.write(recent_file.read())
        os.remove(first_file)
