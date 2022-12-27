import os


def move_file(command: str) -> None:
    command_type, source, destination = command.split()
    with open(source, "r") as old_file:
        if command_type == "mv":
            move_to = destination.split("/")
            path = ""
            for folder in move_to:
                if folder != move_to[-1]:
                    path = os.path.join(path, folder)
                    os.mkdir(path)
            with open(destination, "w") as new_file:
                new_file.write(old_file.read())
                os.remove(source)
