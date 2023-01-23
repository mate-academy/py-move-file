import os


def move_file(command: str) -> None:
    mv, source_file, current_path = command.split()
    if mv == "mv":
        if "/" in current_path:
            path = os.path.dirname(current_path)
            new_file = os.path.basename(current_path)
            os.makedirs(path)
            current_path = os.path.join(path, new_file)
        with open(source_file, "r") as file_read, \
                open(current_path, "w") as file_write:
            file_write.write(file_read.read())
        os.remove(source_file)
