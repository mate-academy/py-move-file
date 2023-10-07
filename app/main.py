import os


def move_file(command: str) -> None:
    action, source_file, destination = command.split()
    if action == "mv":
        destination_dir, destination_filename = os.path.split(destination)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)
        with open(source_file, "r") as source, open(destination, "w") as dest:
            dest.write(source.read())
        os.remove(source_file)
    else:
        os.rename(source_file, destination)
