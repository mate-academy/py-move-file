import os


def move_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) != 3:
        return

    cmd, source_file, destination_file = split_command

    if cmd != "mv" or not os.path.exists(source_file):
        return

    if destination_file.endswith("/"):
        destination_file = os.path.join(destination_file,
                                        os.path.basename(source_file))

    directories = os.path.dirname(destination_file)

    if directories:
        os.makedirs(directories, exist_ok=True)

    with open(source_file, "r") as target_file, open(destination_file,
                                                     "w") as moved_file:
        moved_file.write(target_file.read())

    os.remove(source_file)
