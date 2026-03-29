import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        command, source_file_name, new_file_info = command.split()
        directories, file_name = os.path.split(new_file_info)
        if directories:
            os.makedirs(directories, exist_ok=True)
        with (
            open(source_file_name, "r") as old_file,
            open(new_file_info, "w") as new_file
        ):
            new_file.write(old_file.read())
        os.remove(source_file_name)
