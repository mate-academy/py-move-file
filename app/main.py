import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and len(command.split()) == 3:
        mv_command, first_file, second_file_with_path = command.split()
        directories, second_file = os.path.split(second_file_with_path)
        if directories:
            os.makedirs(directories, exist_ok=True)
        new_file_directory = os.path.join(directories, second_file)
        with (
            open(first_file, "r") as old_file,
            open(new_file_directory, "w") as new_file
        ):
            new_file.write(old_file.read())
        os.remove(first_file)
