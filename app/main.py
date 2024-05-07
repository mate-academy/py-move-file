import os


def move_file(command: str) -> None:

    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        cmd, source, destination = command
        directory = os.path.dirname(destination)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with (
            open(source, "r") as source_file,
            open(destination, "w") as destination_file
        ):
            destination_file.write(source_file.read())
        if os.path.exists(source):
            os.remove(source)

