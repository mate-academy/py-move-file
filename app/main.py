import os


def move_file(command: str) -> None:
    commands = command.strip().split()

    if commands[0] != "mv" or len(commands) != 3:
        raise(
            "Command must have 'mv' and exactly "
            "2 arguments (source and destination)"
        )

    source_file = commands[1]
    destination = commands[2]

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file {source_file} does not exist")

    if destination.endswith('/'):
        if not os.path.exists(destination):
            os.makedirs(destination)
        destination = os.path.join(destination, os.path.basename(source_file))

    else:
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

    os.rename(source_file, destination)
    print(f"Moved {source_file} to {destination}")
