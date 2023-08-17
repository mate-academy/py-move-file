import os


def move_file(command: str) -> None:
    value = command.split()
    if len(value) != 3:
        raise ValueError("Incorrect command line.")
    if value[0] == "mv":
        current = value[1]
        destination = value[2]
        separated = destination.split("/")[:-1]
        directories = "/".join(separated)
        if directories:
            os.makedirs(directories, exist_ok=True)
        with (
            open(current, "r") as current_file,
            open(destination, "w") as destination_file
        ):
            for each_line in current_file:
                destination_file.write(each_line)
        os.remove(current)
