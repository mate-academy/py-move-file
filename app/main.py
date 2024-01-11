import os


def move_file(command) -> None:
    command, source_file, new_file = command.split()
    if command == "mv":
        path, filename = os.path.split(new_file)
        if not path:
            os.replace(source_file, new_file)
        if path:
            if not os.path.exists(path):
                os.mkdir(path)
            os.replace(source_file, new_file)










