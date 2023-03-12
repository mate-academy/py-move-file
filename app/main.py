import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, file_to_read, some_dir_and_file = command.split()
        if command == "mv":
            dir_way, file_to_copy = os.path.split(some_dir_and_file)
            if len(dir_way) != 0:
                os.makedirs(dir_way, exist_ok=True)
                with open(file_to_read, "r") as file_in, \
                        open(dir_way + "/" + file_to_copy, "w") as file_out:
                    file_out.write(file_in.read())
                    os.remove(file_to_read)
            else:
                with open(file_to_read, "r") as file_in, \
                        open(file_to_copy, "w") as file_out:
                    file_out.write(file_in.read())
                    os.remove(file_to_read)
