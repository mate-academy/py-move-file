import os.path


def move_file(command: str) -> None:
    command_in_parts = command.split()
    if len(command_in_parts) != 3:
        return
    if (
        command_in_parts[0] == "mv"
        and command_in_parts[1] != command_in_parts[2]
    ):
        target_directory, file_name = os.path.split(command_in_parts[2])
        if target_directory:
            os.makedirs(target_directory, exist_ok=True)
        with (
            open(command_in_parts[2], "w") as new_file,
            open(command_in_parts[1], "r") as old_file
        ):
            new_file.write(old_file.read())
        os.remove(command_in_parts[1])
