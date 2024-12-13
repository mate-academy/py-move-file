import os


def move_file(command: str) -> None:
    splitted_command = command.split()
    if splitted_command[0] == "mv":
        source_file = splitted_command[1]
        new_file = splitted_command[2]
        if new_file.count("/") > 0:
            slice_ = splitted_command[2].rfind("/")
            new_file = splitted_command[2][slice_ + 1:]
            current_path = splitted_command[2][:slice_]
            os.makedirs(current_path)
            new_file = os.path.join(current_path, new_file)
        with open(source_file, "r") as file_read, \
                open(new_file, "w") as file_write:
            text = file_read.read()
            file_write.write(text)
        os.remove(source_file)
