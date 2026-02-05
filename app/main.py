import os


def move_file(command: str) -> None:
    mv_command, old_file, path = command.split()

    if mv_command == "mv":

        with open(old_file, "r") as file:
            file_data = file.read()
        dirs_and_file = path.split("/")

        dirs = []
        new_file_name = ""

        for dir_ in dirs_and_file:
            if ".txt" in dir_:
                new_file_name += dir_
            else:
                dirs.append(dir_)

        dir_path = ""
        for dir_ in dirs:
            dir_path += dir_
            os.makedirs(dir_path, exist_ok=True)
            dir_path += "/"
        file_path = os.path.join(dir_path, new_file_name)

        with open(file_path, "w") as file:
            file.write(file_data)
        os.remove(old_file)

    return
