import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv" and len(command.split()) == 3:
        file_to_read, file_to_write = command.split()[1:]
        with open(file_to_read, "r") as file_read:
            context = file_read.read()
        if "/" not in file_to_write:
            with open(file_to_write, "w") as file_write:
                file_write.write(context)
        else:
            directories = file_to_write.split("/")
            directories, new_file = directories[:-1], directories[-1]
            path = os.path.join(*[*directories])
            os.makedirs(path)
            with open(os.path.join(path, new_file), "w") as file_write:
                file_write.write(context)
        os.remove(file_to_read)
    else:
        raise ValueError("command must be in format: 'mv file1.txt file2.txt'")
