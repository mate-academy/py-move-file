import os


def move_file(command: str) -> None:
    command = command.split()
    file_name = command[1]
    destination = command[2]

    if "/" not in destination:
        os.rename(file_name, destination)
    else:
        directory = os.path.dirname(destination)
        os.makedirs(directory, exist_ok=True)

        with open(file_name, "r") as old_file:
            with open(destination, "w") as new_file:
                new_file.write(old_file.read())
        os.remove(file_name)
