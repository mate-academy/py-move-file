import os


def move_file(command: str) -> None:
    mv, original_file, new_file = command.split()
    if mv == "mv":
        if "/" in new_file:
            dir_list = new_file.split("/")
            dir_list.remove(dir_list[-1])
            dir_path = "/".join(dir_list)
            os.makedirs(dir_path)
            new_file = os.path.join(dir_path, new_file)
        with open(original_file, "r") as file_in, \
                open(new_file, "w") as file_out:
            file_out.write(file_in.read())
            os.remove(original_file)
