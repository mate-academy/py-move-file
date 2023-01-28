import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv":
        file_to_read, file_to_write = command.split()[1:]
        old_file = file_to_read
        path = ""

        with open(file_to_read, "r") as file_read:
            context = file_read.read()
            if "/" not in file_to_write:
                with open(file_to_write, "w") as file_write:
                    file_write.write(context)
            else:
                directories = file_to_write.split("/")[:-1]
                new_file = file_to_write.split("/")[-1]
                for directory in directories:
                    path = os.path.join(path, directory)
                    os.mkdir(path)
                with open(os.path.join(path, new_file), "w") as file_write:
                    file_write.write(context)
            os.remove(old_file)
