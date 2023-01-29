import os


def move_file(command: str) -> None:
    mv, original_file, new_file = command.split()
    if mv == "mv":
        if "/" in new_file:
            dir_tuple = os.path.split(new_file)
            dir_path = dir_tuple[1]
            os.makedirs(dir_path)
            new_file = os.path.join(dir_path, new_file)
        with open(original_file, "r") as file_in, \
                open(new_file, "w") as file_out:
            file_out.write(file_in.read())
            os.remove(original_file)
