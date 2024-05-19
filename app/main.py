import os


def move_file(command: str) -> None:
    command = command.split()
    cmd, old_loc, new_loc = command
    new_directory = os.path.dirname(new_loc)
    if new_directory:
        os.makedirs(new_directory, exist_ok=True)
    with (open(old_loc, "r") as source_file,
            open(new_loc, "w") as destination_file):
        destination_file.write(source_file.read())
    if os.path.exists(old_loc):
        os.remove(old_loc)
