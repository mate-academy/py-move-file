import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and len(command.split()) == 3:
        command, source_file_name, new_file_info = command.split()
        directories, file_name = os.path.split(new_file_info)
        if directories:
            os.makedirs(directories, exist_ok=True)
        new_file_name = os.path.join(directories, file_name)
        with (
            open(source_file_name, "r") as old_file,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(old_file.read())
        os.remove(source_file_name)
