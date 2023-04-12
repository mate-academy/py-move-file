import os.path


def move_file(command: str) -> None:
    command_in_parts = command.split(" ")
    target_directory_parts = command_in_parts[2].split("/")
    target_directory_parts.pop(-1)
    if (
        len(command_in_parts) == 3
        and command_in_parts[0] == "mv"
        and os.path.exists(command_in_parts[1])
    ):
        existing_directory = ""
        for directory in target_directory_parts:
            existing_directory += directory
            if not os.path.exists(existing_directory):
                os.mkdir(existing_directory)
            existing_directory += "/"
        with (
            open(command_in_parts[2], "w") as new_file,
            open(command_in_parts[1], "r") as old_file
        ):
            new_file.write(old_file.read())
        os.remove(command_in_parts[1])
