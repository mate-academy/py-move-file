import os


def move_file(command: str) -> None:
    mv, source_file, current_path = command.split()
    if mv == "mv":
        if "/" in current_path:
            last_slash = current_path.rfind("/")
            new_file = current_path[last_slash + 1:]
            os.makedirs(current_path[:last_slash])
            current_path = os.path.join(current_path[:last_slash], new_file)
        with open(source_file, "r") as file_read, \
                open(current_path, "w") as file_write:
            file_write.write(file_read.read())
        os.remove(source_file)
