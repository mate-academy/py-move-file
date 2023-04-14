import os.path


def move_file(command: str) -> None:
    command_in_parts = command.split(" ")
    if len(command_in_parts) != 3:
        return
    target_directory = os.path.dirname(command_in_parts[2])
    if (
        command_in_parts[0] == "mv"
        and os.path.exists(command_in_parts[1])
    ):
        existing_directory = ""
        target_directory_parts = target_directory.split("/")
        for directory in target_directory_parts:
            existing_directory = os.path.join(existing_directory, directory)
            if not os.path.exists(existing_directory):
                os.makedirs(existing_directory, exist_ok=True)
        with (
            open(command_in_parts[2], "w") as new_file,
            open(command_in_parts[1], "r") as old_file
        ):
            new_file.write(old_file.read())
        os.remove(command_in_parts[1])
