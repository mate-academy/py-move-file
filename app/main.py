import os


def move_file(command: str) -> None:
    command_parts = command.split()

    if command_parts[0] != "mv" or len(command_parts) != 3:
        raise ValueError("Incorrect command input.")

    old_file, new_file = command_parts[1:]

    if new_file.endswith("/"):
        raise ValueError("It mustn't be considered as a directory")

    destination_directory = os.path.dirname(new_file)

    if destination_directory and not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    with (open(old_file, "r") as source_file,
          open(new_file, "w") as destination_file):
        destination_file.write(source_file.read())

    if os.path.exists(new_file):
        os.remove(old_file)
